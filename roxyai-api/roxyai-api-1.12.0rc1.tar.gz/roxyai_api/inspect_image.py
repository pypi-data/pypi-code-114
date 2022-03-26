# (c) Roxy Corp. 2020-
# Roxy AI Coordinator
from __future__ import annotations
from typing import Optional, Tuple, Union, NamedTuple
from enum import IntEnum
import numpy as np
import struct
import cv2
import traceback
from pathlib import Path
from io import BytesIO

from logging import getLogger
log = getLogger(__name__)


class ImageRect(NamedTuple):
    """ 領域指定用NamedTupleクラス
    """
    x1: int = 0
    y1: int = 0
    x2: int = 0
    y2: int = 0


class ImageConvertionFailed(RuntimeWarning):
    """ 画像変換エラー
    """
    def __init__(self, src_fmt, dst_fmt, order, exception):
        if type(src_fmt) is int:
            src_fmt = ImageFormat(src_fmt)
        self.src_fmt = src_fmt

        if type(dst_fmt) is int:
            dst_fmt = ImageFormat(dst_fmt)
        self.dst_fmt = dst_fmt

        if type(order) is int:
            order = ColorOrder(order)
        self.order = order

        self.exception = exception

    def __str__(self):
        return (
            f'image conversion failed '
            f'from [{self.src_fmt.name}] '
            f'to [{self.dst_fmt.name}] '
            f'color order: {self.order.name}'
        )


class ImageFormat(IntEnum):
    """ イメージフォーマット値の定義クラス
    """
    RAW = 0x01
    JPEG = 0x02
    PNG = 0x03
    BMP = 0x04
    # 内部利用のフォーマット形式
    NDARRAY = 0xFF

    def __str__(self):
        return f'{self.name}(0x{self.value:02X})'

    @property
    def suffix(self) -> str:
        return IMG_FORMAT_SUF(self.value)

    @staticmethod
    def all_suffix(header: str = None) -> tuple:
        if header is None:
            return IMG_SUFFIX_LIST
        return tuple(header + s for s in IMG_SUFFIX_LIST)

    @classmethod
    def from_suffix(cls, suffix: str) -> ImageFormat:
        """ 拡張子からフォーマット値を取得
        Args:
            suffix (str)    拡張子文字列
        Returns:
            ImageFormat:    拡張子に対応するフォーマット値
            None:           拡張子が不正
        """
        suf = suffix.lower()
        if suf and suf[0] != '.':
            suf = '.' + suf
        val = IMG_SUFFIX_FMT.get(suf)
        if val:
            return cls(val)
        return None

    @classmethod
    def check_header(cls, data: memoryview):
        """ 画像データのヘッダからフォーマットを取得
        Args:
            data:   画像データのヘッダ
        Returns:
            ImageFormat:    解析成功
            None:           解析失敗
        Note:
            data は bytes でも良い。
        """
        size = len(data)

        # PNGフォーマット(http://www.w3.org/TR/PNG/)の読み取り
        # ※ 古いPNGフォーマットは非対応
        if (size >= 8) and (data[:8] == b'\x89PNG\r\n\x1A\n'):
            return cls.PNG
        if (size > 2) and (data[:2] == b'BM'):
            return cls.BMP
        if (size > 4) and (data[:2] == b'\xFF\xD8'):
            return cls.JPEG
        return None


class ColorOrder(IntEnum):
    """ Rawイメージの色データバイト順の定義クラス
    """
    GRAY = 1
    BGR = 2
    RGB = 3
    BGRA = 4

    @property
    def depth(self):
        """ 色順序による色深度（ピクセルあたりバイト数）
        """
        if self == ColorOrder.GRAY:
            ret = 1
        elif self in (ColorOrder.BGR, ColorOrder.RGB):
            ret = 3
        elif self == ColorOrder.BGRA:
            ret = 4
        return ret

    def __str__(self):
        return f'{self.name}({self.value:d})'


# フォーマット変換の定義
IMG_FORMAT_SUF = {
    ImageFormat.RAW: '.bin',
    ImageFormat.JPEG: '.jpg',
    ImageFormat.PNG: '.png',
    ImageFormat.BMP: '.bmp',
}

IMG_SUFFIX_LIST = tuple(IMG_FORMAT_SUF.values())

IMG_SUFFIX_FMT = {
    **{v: ImageFormat(k) for k, v in IMG_FORMAT_SUF.items()},
    '.jpeg': ImageFormat(ImageFormat.JPEG),
}

# CVの変換用パラメータ定義
__JPEG_PARAMS = (cv2.IMWRITE_JPEG_QUALITY, 95)
__PNG_PARAMS = (cv2.IMWRITE_PNG_COMPRESSION, 1)


def _bin_to_ndarary(src):
    # 構造情報の設定
    width, height, order = struct.unpack('< H H B', src[:5])
    dt = np.dtype('uint8')
    dt = dt.newbyteorder('<')
    dst: np.ndarray = np.frombuffer(src, dtype=dt, offset=5)
    depth = ColorOrder(order).depth
    if depth == 1:
        dst = dst.reshape((height, width))
    else:
        dst = dst.reshape((height, width, depth))
    return dst, ColorOrder(order)


def _image_to_ndarary(src):
    dt = np.dtype('uint8')
    dt = dt.newbyteorder('<')
    buf = np.frombuffer(src, dtype=dt, offset=0)
    dst: np.ndarray = cv2.imdecode(buf, cv2.IMREAD_IGNORE_ORIENTATION | cv2.IMREAD_UNCHANGED)
    if len(dst.shape) == 2:
        order = ColorOrder.GRAY
    elif dst.shape[2] == 3:
        # CVは24bitをBGRの色順で保持
        order = ColorOrder.BGR
    elif dst.shape[2] == 4:
        # CVは32bitをBGRAの色順で保持
        order = ColorOrder.BGRA
    return dst, ColorOrder(order)


def _ndarary_to_bin(src: np.ndarray, order: ColorOrder) -> bytes:
    shape = (src.shape[1], src.shape[0], order)
    dst = struct.pack('< H H B', *shape)
    dst += src.tobytes()
    return dst


def _ndarary_to_jpeg(src, order: ColorOrder) -> bytes:
    if order == ColorOrder.RGB:
        # CV2の色順に変換
        src = cv2.cvtColor(src, cv2.COLOR_RGB2BGR)
    ret, dst = cv2.imencode('.jpg', src, params=__JPEG_PARAMS)
    if not ret:
        RuntimeWarning('imencode for jpg failed')
    return bytes(np.frombuffer(dst, dtype=np.uint8))


def _ndarary_to_png(src, order: ColorOrder) -> bytes:
    if order == ColorOrder.RGB:
        # CV2の色順に変換
        src = cv2.cvtColor(src, cv2.COLOR_RGB2BGR)
    ret, dst = cv2.imencode('.png', src, params=__PNG_PARAMS)
    if not ret:
        RuntimeWarning('imencode for png failed')
    return bytes(np.frombuffer(dst, dtype=np.uint8))


def _ndarary_to_bmp(src, order: ColorOrder) -> bytes:
    if order == ColorOrder.RGB:
        # CV2の色順に変換
        src = cv2.cvtColor(src, cv2.COLOR_RGB2BGR)
    ret, dst = cv2.imencode('.bmp', src)
    if not ret:
        RuntimeWarning('imencode for bmp failed')
    return bytes(np.frombuffer(dst, dtype=np.uint8))


class ImageBuffer(BytesIO):
    name = 'Buffer'

    def __init__(self, *args, **kwargs):
        """ 分割受信用有りの画像専用バッファ
        """
        super().__init__(*args, **kwargs)

    def close(self, release: bool = None):
        # 通常の書き込み完了時にはクローズさせない
        if release:
            super().close()
        return


class InspectImage():
    """ 検査に利用するイメージデータのキャッシュ機能付き管理クラス
    """
    DECODER = {
        ImageFormat.RAW: _bin_to_ndarary,
        ImageFormat.JPEG: _image_to_ndarary,
        ImageFormat.PNG: _image_to_ndarary,
        ImageFormat.BMP: _image_to_ndarary,
    }

    ENCODER = {
        ImageFormat.RAW: _ndarary_to_bin,
        ImageFormat.JPEG: _ndarary_to_jpeg,
        ImageFormat.PNG: _ndarary_to_png,
        ImageFormat.BMP: _ndarary_to_bmp,
    }

    def __init__(
        self,
        fmt: ImageFormat,
        data: bytes,
        path: Optional[Path] = None,
        order: ColorOrder = None,
        name: str = '',
    ):
        """ 検査用の画像データ管理
        Args:
            fmt     data で渡す画像のフォーマット
                    不明は場合は None で指定
            data:   画像データ
            path    読み込んだ元ファイルのパス
            order:  画像の色データバイト順
            name:   画像の識別名称
        """
        self._org_fmt = ImageFormat(fmt)
        self._data = {self._org_fmt: data}

        self._path = path
        self._name = name
        if not name:
            # 名前の指定が無ければ自動で定義
            path_name = None
            try:
                path_name = Path(path).name
            except Exception:
                pass
            if path_name:
                # 名称が未指定でパスがある場合はファイル名を設定
                self._name = path_name
            else:
                self._name = f'image[{self._org_fmt.name}]'
        self._keep_count = 1
        if order is None:
            if fmt == ImageFormat.NDARRAY:
                if len(data.shape) == 2:
                    order = ColorOrder.GRAY
                elif data.shape[2] == 3:
                    # CVは24bitをBGRの色順で保持
                    order = ColorOrder.BGR
                elif data.shape[2] == 4:
                    # CVは32bitをBGRAの色順で保持
                    order = ColorOrder.BGRA
        self._order = order
        # キャッシュ管理情報
        self._parent = None
        self._children = []
        self._zoom = None
        self._clip = None
        # バッファ管理情報
        self._src_buffer: BytesIO = None
        self._src_view: memoryview = None
        self._src_size = 0

    @classmethod
    def get_empty(
        cls,
        width: int = 1,
        height: int = 1,
        color: Union[tuple[int, int, int], tuple[int, int, int, int], int] = (0, 0, 0)
    ) -> InspectImage:
        """ 空のイメージを取得する
        Args:
            width:      画像の幅ピクセル数
            height:     画像の高さピクセル数
            colose:     塗りつぶし色
                (int, int, int):         RGB画像として作成(3ch)
                (int, int, int, int):    RGBA画像として作成(4ch)
                int:                     Gray画像として作成(1ch)
        """
        if (type(color) is int):
            order = ColorOrder.GRAY
        elif len(color) == 1:
            color = color[0]
            order = ColorOrder.GRAY
        elif len(color) == 3:
            order = ColorOrder.RGB
        elif len(color) == 4:
            order = ColorOrder.BGRA
        else:
            raise TypeError(f'{cls.__name__}: invalid color parameter {color}')

        if order == ColorOrder.GRAY:
            data = np.full((height, width), color, np.uint8)
        else:
            data = np.full((height, width, order.depth), color, np.uint8)
        instance = InspectImage(ImageFormat.NDARRAY, data, order=order)
        return instance

    @classmethod
    def from_buffer(cls, buffer: BytesIO, name: str = None) -> InspectImage:
        """ バッファから画像を取得する
        Args:
            buffer:     データバッファ
            name:       ファイル名（パス指定）
        Notes:
            バッファへの読み込みが完了していない場合は
            バッファへの書き込み後に flush_buffer する必要がある。
        """
        instance = None
        completed = None
        with buffer.getbuffer() as view:
            completed = cls.check_data(view)
        if completed:
            # 読み込み完了済みならば初期化
            view = buffer.getbuffer()
            fmt = ImageFormat.check_header(view)
            instance = cls(fmt, view, name=name)
            instance._src_buffer = buffer
            instance._src_size = len(view)
            instance._src_view = view

        return instance

    @classmethod
    def load(cls, path) -> InspectImage:
        """ ファイルから画像を読み込む
        """
        instance = None
        imgfile = Path(path)
        if imgfile.exists():
            data = imgfile.read_bytes()
            completed = cls.check_data(data)
            if completed:
                fmt = ImageFormat.check_header(data)
                instance = cls(fmt, data, path=imgfile)
        return instance

    def save(self, path) -> bool:
        """ ファイルに画像を書き込む
        Returns:
            True:   書き込み成功
            False:  書き込み失敗
        Note:
            ファイル名の拡張子で画像フォーマットを決定する
        """
        imgfile = Path(path)
        fmt = IMG_SUFFIX_FMT.get(imgfile.suffix)
        if fmt:
            data = self.get_image(fmt)
            if data:
                imgfile.write_bytes(data)
                if not self._path:
                    # ファイルパスが未登録ならばパス登録
                    self._path = imgfile
                return True
        return False

    def get_tf_image(self) -> np.ndarray:
        """ TensorFlow用のデータ取得
        """
        img = self.get_image()
        # ndarrayがTF形式RGB(24bit)でなければ変換
        if self._order == ColorOrder.GRAY:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        elif self._order == ColorOrder.BGR:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        elif self._order == ColorOrder.BGRA:
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
        return img

    def get_image(
        self, fmt: ImageFormat = ImageFormat.NDARRAY,
    ) -> Union[np.ndarray, bytes, None]:
        """ 指定フォーマトの画像データを取得
        """
        img = self._data.get(fmt)
        if img is not None:
            # 対象フォーマットがキャッシュにあればそれを返す
            return img
        # 無ければ画像変換してそれを返す
        self.__convert(fmt)
        img = self._data.get(fmt)
        return img

    def get_size(self, fmt: ImageFormat = None) -> int:
        """ 指定フォーマットのデータサイズを取得
        """
        fmt = ImageFormat(fmt)
        img = self.get_image(fmt)
        if img is None:
            return None
        if fmt == ImageFormat.NDARRAY:
            return img.size
        else:
            return len(img)

    def __convert(self, fmt: ImageFormat = ImageFormat.NDARRAY):
        """ 画像フォーマット変換
        """
        if self._data.get(fmt) is not None:
            # 変換済みなら何もしない
            return

        if self._order is None:
            # 基準データ(ndarray)の作成
            src = self._data.get(self._org_fmt)
            try:
                if (src is None) and self._src_buffer:
                    # バッファからの読み込み途中の場合はビューから変換
                    self._src_buffer.flush()
                    with self._src_buffer.getbuffer() as view:
                        fmt = ImageFormat.check_header(view)
                        converter = self.DECODER[fmt]
                        dst, order = converter(view)
                else:
                    converter = self.DECODER[self._org_fmt]
                    dst, order = converter(src)
            except Exception as e:
                log.warning(traceback.format_exc())
                raise ImageConvertionFailed(self._org_fmt, ImageFormat.NDARRAY, None, e)
            self._data[ImageFormat.NDARRAY] = dst
            self._order = order

        if fmt != ImageFormat.NDARRAY:
            # 基準データ(ndarray)から変換先の画像データの作成
            src = self._data[ImageFormat.NDARRAY]
            converter = self.ENCODER[fmt]
            try:
                dst = converter(src, self._order)
            except Exception as e:
                log.warning(traceback.format_exc())
                raise ImageConvertionFailed(ImageFormat.NDARRAY, fmt, self._order, e)
            self._data[fmt] = dst

    def keep(self):
        """ 画像データを保持する(TBD)
        """
        self._keep_count += 1

    def release(self):
        """ 画像データを全て破棄する(TBD)
        """
        self._keep_count -= 1
        if self._keep_count > 0:
            # まだ保持している処理があるので破棄しない
            return
        self._data.clear()
        self._org_fmt = None
        if self._fnc_buf_release:
            # バッファの解放コールバックの呼び出し
            try:
                self._fnc_buf_release()
            except Exception as e:
                log.warning(
                    f'{e}: in callback for release image buffer: '
                    f'{self._fnc_buf_release()} '
                    f'<{self._name}>'
                )
            self._fnc_buf_release = None

    def get_clipped(
        self,
        area: ImageRect,
    ) -> InspectImage:
        """ 領域をクリップしたイメージオブジェクトを返す
        """
        area = ImageRect(*area)
        # キャッシュ探索
        che = [i for i in self._children if i._clip == area]
        if che:
            return che[0]
        # 画像生成
        org = self.get_image()
        buf = org[area.y1:area.y2, area.x1:area.x2]
        img = InspectImage(ImageFormat.NDARRAY, buf)
        # キャッシュ情報登録
        img._parent = self
        img._clip = area
        self._children.append(img)
        return img

    def get_resized(self, width: int, height: int) -> InspectImage:
        """ 画像をリサイズしたイメージオブジェクトを返す
        """
        # キャッシュの探索
        target_shape = (height, width)
        che = [i for i in self._children if i.get_image().shape == target_shape]
        if che:
            return che[0]
        # 画像生成
        org = self.get_image()
        buf = cv2.resize(org, (width, height))
        img = InspectImage(ImageFormat.NDARRAY, buf)
        # キャッシュ情報登録
        img._parent = self
        self._children.append(img)
        return img

    def get_grayed(self) -> InspectImage:
        """ 画像をグレースケール化したイメージオブジェクトを返す
        """
        if self.order is ColorOrder.GRAY:
            # グレースケール画像ならばそのまま利用
            img = self
        else:
            # キャッシュの探索
            che = [i for i in self._children if i._order is ColorOrder.GRAY]
            if che:
                return che[0]
            # 画像生成
            org = self.get_image()
            if self._order is ColorOrder.RGB:
                cvt_code = cv2.COLOR_RGB2GRAY
            elif self._order is ColorOrder.BGR:
                cvt_code = cv2.COLOR_BGR2GRAY
            elif self._order is ColorOrder.BGRA:
                cvt_code = cv2.COLOR_BGRA2GRAY
            else:
                log.warning(f'invalid color order {self._order} in <{self._name}>')
                cvt_code = None
            try:
                buf = cv2.cvtColor(org, cvt_code)
                img = InspectImage(ImageFormat.NDARRAY, buf)
                # キャッシュ情報登録
                img._parent = self
                self._children.append(img)
            except Exception as e:
                log.warning(traceback.format_exc())
                raise ImageConvertionFailed(
                    self._org_fmt, ImageFormat.NDARRAY, ColorOrder.GRAY, e
                )
        return img

    def show_window(self):
        """ 画像のウィンドウ表示（開発用）
        """
        img = self.get_image()
        cv2.imshow(str(self._path), img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def release_buffer(self):
        if self._src_view:
            # ビューデータを削除
            self._src_view.release()
            self._data.pop(self._org_fmt)
        if self._src_buffer:
            # バッファをクローズ
            self._src_buffer.close(release=True)
            self._src_buffer = None

    # 読み取り専用のパラメータアクセス定義
    @property
    def format(self) -> int:
        return self._org_fmt

    @property
    def data(self) -> int:
        return self._data

    @property
    def path(self) -> Path:
        return self._path

    @property
    def name(self) -> str:
        return self._name

    @property
    def parent(self) -> InspectImage:
        return self._parent

    @property
    def zoom(self) -> float:
        return self._zoom

    @property
    def order(self) -> ColorOrder:
        return self._order

    @property
    def width(self) -> int:
        """ 画像の幅のピクセル数
        """
        return self.get_image().shape[1]

    @property
    def height(self) -> int:
        """ 画像の幅のピクセル数
        """
        return self.get_image().shape[0]

    @property
    def buffer(self) -> BytesIO:
        return self._src_buffer

    @staticmethod
    def get_merged(images: Tuple[InspectImage]) -> InspectImage:
        """ 画像をグレースケール化したイメージオブジェクトを返す
        """
        # 画像生成
        try:
            src_data = []
            for img in images:
                img_data = img.get_image()
                if img_data.dtype == np.uint16:
                    img_data = (img_data // 0x100).astype(np.uint8)
                src_data.append(img_data)
            buf = cv2.merge(src_data)
            new_name = '_'.join(img.name for img in images if img.name)
            img = InspectImage(ImageFormat.NDARRAY, buf, name=new_name)
        except Exception as e:
            imgs_str = ', '.join(str(img._name) for img in images)
            log.warning(f'Failed to merge images ({imgs_str})\n{e}')
            img = None
        return img

    @staticmethod
    def check_data(data) -> bool:
        """ バッファのデータサイズをチェック
        Args:
            data:       チェックするバイナリ
        Returns:
            True:       全画像データ取得済み
            False:      全画像データ取得未完了
        Note:
            バッファ操作でメモリ確保を行わない
        """
        size = len(data)
        format = ImageFormat.check_header(data)
        length = 0

        # PNGフォーマット確認
        if (
            format == ImageFormat.PNG
            and (size >= 24)
            and (data[12:16] == b'IHDR')
        ):
            # PNGファイルサイズの推測（データの存在する範囲で計算）
            length = 8 + 25     # Signature + IHDR
            while length + 8 <= size:
                # 読み出すチャンクがまだ存在するならば
                l, = struct.unpack('> L', data[length:length + 4])
                ctype = data[length + 4:length + 8]
                length += int(l) + 12       # Lenght + ChunkType + CRC (12bytes)

                # 解析用のログ出力を行う場合
                # from logging import DEBUG
                # if log.root.level <= DEBUG:
                #     # デバグ出力有りの場合
                #     if type(ctype) is memoryview:
                #         bdata = ctype.tobytes()
                #     else:
                #         bdata = ctype
                #     log.debug(f'    PNG chunk {bdata.decode()} [{length:,} bytes]')

                if ctype == b'IEND':
                    # 終端なので解析終了
                    break
            if ctype != b'IEND':
                # 終端チャンク未到達ならば足し合わせる
                length += 12

        # BMPフォーマット確認
        elif (
            format == ImageFormat.BMP
            and (size >= 6)
        ):
            # PNGファイルのデータ読み取り
            format = ImageFormat.BMP
            l, = struct.unpack('< L', data[2:6])
            length = int(l)

        # JPEGフォーマット確認(TBD)
        elif (
            format == ImageFormat.JPEG
        ):
            # 暫定でJPEGは常に読み取り完了済みとする
            length = size

        # 受信サイズの方が大きい場合は読込完了とする
        return (length <= size)

    def __str__(self):
        if self._name:
            text = f'"{self._name}"'
        else:
            text = 'Image'
        text += f'({self.width}, {self.height}): '
        cached = [
            f'{ImageFormat(fmt).name} '
            f'{len(self._data.get(fmt)):,d} bytes'
            for fmt in IMG_FORMAT_SUF
            if type(self._data.get(fmt)) is bytes
        ]
        if self._order:
            # 基準データ(ndarray)作成済み
            raw = self._data.get(ImageFormat.NDARRAY)
            cached.append(
                f'{ImageFormat.NDARRAY.name}-'
                f'{self._order.name} '
                f'{raw.size:,d} bytes'
            )
        text += ', '.join(cached)
        if self._path:
            try:
                path = Path(self._path).resolve().absolute().as_posix()
            except Exception:
                path = str(self._path)
            # ファイルに紐づいている場合
            text += f', path: {path}'
        return text
