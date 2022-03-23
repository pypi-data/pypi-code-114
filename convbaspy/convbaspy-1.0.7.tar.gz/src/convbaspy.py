"""
**modificado desde el original : -> examples/calculator.py
https://github.com/Textualize/textual


    github.com/etensor/baseconvpy
La documentación de la libreria es muy escasa y sus alcances se ocultan
entre los ejemplos del autor.

        Conversor de Bases
       --------------------

#David Penilla
#github.com/etensor

"""

from decimal import Decimal
from rich.align import Align
from rich.console import Console, ConsoleOptions, RenderResult, RenderableType
from rich.padding import Padding
from rich.text import Text
from textual.app import App
from textual.reactive import Reactive
from textual.views import GridView
from textual.widget import Widget
from textual.widgets import Button, ButtonPressed, Footer, ScrollView
from textual import events
from pyfiglet import Figlet, figlet_format
import pyperclip
from typing import Callable

from conversor import Conversor
from docs import codigo_fuente



class FigletText:   # para autoescalar el texto

    def __init__(self, text: str) -> None:
        self.text = text

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        """Build a Rich renderable to render the Figlet text.

                Rich render==>figlet
        """
        size = min(options.max_width / 2, options.max_height)
        if size < 4:
            yield Text(self.text, style="light")
        else:
            if size < 7:
                font_name = "mini"
            elif size < 9:
                font_name = "small"
            elif size < 12:
                font_name = "standard"
            else:
                font_name = "big"
            font = Figlet(font=font_name, width=options.max_width)
            yield Text(font.renderText(self.text).rstrip("\n"), style="bold")


class EleganTexto(Widget):

    texto = ""
    style = Reactive("")
    mouse_over = Reactive(False)
    fx : Callable #= print # depronto una funcion primitiva mas liviana
    base : int = 0
    

    def __init__(self, texto, style="yellow on rgb(20,40,20)", funcional=False,func_x: Callable=str(),bT : int = 0):
        super().__init__()
        self.texto = texto
        self.style = style
        if funcional:
            self.fx = func_x
            self.base = bT
    
    async def on_enter(self, event: events.Enter) -> None:
        self.mouse_over = True

    async def on_leave(self, event: events.Leave) -> None:
        self.mouse_over = False

    async def on_focus(self, event: events.Focus) -> None:
        if self.base != 0:
            self.fx(self.base)
        else:
            pass # a menos que se use para otro proposito


    def render(self) -> RenderableType:
        
        return Padding(
            Align.center(FigletText(self.texto), vertical="middle"),
            (0,1),
            style=self.style if not self.mouse_over else 'white on blue',
        )


class Numbers(Widget):
    """digital display
        Aqui tomamos 4 para las bases 2,8,10,16 y IEEE754 - 32,64 bits
    """

    value = Reactive("0.0")
    mouse_over = Reactive(False)

    async def on_enter(self, event: events.Enter) -> None:
        self.mouse_over = True

    async def on_leave(self, event: events.Leave) -> None:
        self.mouse_over = False

    async def on_focus(self,event: events.Focus) -> None:
        self.has_focus = True
        pyperclip.copy(self.value)

    
    def render(self) -> RenderableType:
        """Build a Rich renderable to render the calculator display.

            este metodo retorna un renderizable compatible con textual

        """  # Padding <- [Renderizable]
        return Padding(
            Align.center(FigletText(self.value), vertical="middle"),
            (0, 1),
            style="rgb(236,206,0) on rgb(0,0,0)" \
            if not self.mouse_over else "white on rgb(50,50,50)",
        )


class Calculator(GridView):
    """A working calculator app.

        Modificada calculadora para el conversor de bases
        Métodos Númericos
        -----------------


    """

    DARK = "white on rgb(51,51,51)"
    LIGHT = "red on rgb(32,32,32)"
    YELLOW = "white on rgb(255,159,7)"

    BUTTON_STYLES = {
        "AC": YELLOW,
        "C": DARK,
        "+/-": LIGHT,
    }

    display = Reactive("0")
    show_ac = Reactive(True)
    modo_c  = Reactive('estandar')  # modos -> estandar, 32bit, 64bit

    conversor = Conversor()


    vect_bases = [10,2,8,16]

    def watch_display(self, value: str) -> None:
        """Called when self.display is modified."""
        # self.numbers is a widget that displays the calculator result
        # Setting the attribute value changes the display
        # This allows us to write self.display = "100" to update the display
        # =>> watch: update valor del display [   0.0   ]

        if self.modo_c == 'estandar':
            idx = self.getbaseT_idx()
            if idx <= 3:
                self.display = self.numbers[idx].value = value
  
            for ix in range(len(self.numbers)):
                if ix != idx:
                    self.numbers[ix].value = self.conversor.convertirNM(
                        self.value,
                        self.baseT,
                        self.vect_bases[ix]
                        )
            
            num_dec = self.conversor.convertirNM(self.display,self.baseT,10)
            if self.value not in ('', '0.0'):
                self.ieee32num.value,s32 = self.conversor.dec_ieee3264(num_dec,mod=32)
                self.ieee64num.value,s64 = self.conversor.dec_ieee3264(num_dec,mod=64)

                self.exp32n.value,aux32 = self.conversor.ieee3264_2n(str(self.ieee32num.value),s32)
                self.exp64n.value,aux64 = self.conversor.ieee3264_2n(str(self.ieee64num.value),s64)    

                self.mnt32dec.value = '32bit: '+aux32
                self.mnt64dec.value = '64bit: '+aux64

            else:
                self.ieee32num.value= '0'
                self.ieee64num.value= '0'
                self.mnt32dec.value = '0'
                self.mnt64dec.value = '0'
            

        elif self.modo_c == '32bit':
            shift_m = self.conversor.bin_ieee_dec_shift(
                self.value + '0'*(33-len(value)), 32)

            _,dec_num = self.conversor.ieee3264_2n(
                self.value + '0'*(33-len(value)),
                shift=shift_m
            )

            self.numbers[0].value = dec_num
            for idx in range(1,4):
                self.numbers[idx].value = self.conversor.convertirNM(dec_num,10,self.vect_bases[idx])
            

            ieee64 = self.conversor.dec_ieee3264(dec_num,64)[0].replace(' ','')
            ieee64 += '0'*(64-len(ieee64))

            self.ieee32num.value = self.value + '0'*(33-len(value))
            self.ieee32num.value = f'{self.ieee32num.value[0]} {self.ieee32num.value[1:10]} {self.ieee32num.value[10:]}'
            self.ieee64num.value = f'{ieee64[0]} {ieee64[1:13]} {ieee64[13:]}'
            self.exp32n.value,self.mnt32dec.value  = (str(shift_m),f'32|float: {dec_num}')
            self.exp64n.value, self.mnt64dec.value = self.conversor.ieee3264_2n(self.value + '0'*(33-len(value)), shift=self.conversor.bin_ieee_dec_shift(
                self.value + '0'*(33-len(value)), 32))

        elif self.modo_c == '64bit':
            shift_m = self.conversor.bin_ieee_dec_shift(
                self.value + '0'*(65-len(value)), 64)

            _,dec_num = self.conversor.ieee3264_2n(
                self.value + '0'*(65-len(value)),
                shift=shift_m
            )

            self.numbers[0].value = dec_num
            for idx in range(1, 4):
                self.numbers[idx].value = self.conversor.convertirNM(dec_num, 10,self.vect_bases[idx])


            ieee32 = self.conversor.dec_ieee3264(dec_num, 32)[0].replace(' ','')
            ieee32 += '0'*(32-len(ieee32))

            self.ieee64num.value = self.value + '0'*(65-len(value))
            self.ieee64num.value = f'{self.ieee64num.value[0]} {self.ieee64num.value[1:13]} {self.ieee64num.value[13:]}'
            self.ieee32num.value = f'{ieee32[0]} {ieee32[1:10]} {ieee32[10:]}'
            self.exp64n.value, self.mnt64dec.value = (str(shift_m), f'64|double : {dec_num}')
            self.exp32n.value, self.mnt32dec.value = self.conversor.ieee3264_2n(self.value + '0'*(65-len(value)), shift=self.conversor.bin_ieee_dec_shift(
                self.value + '0'*(65-len(value)), 64))


        return None



    def compute_show_ac(self) -> bool:
        """Compute show_ac reactive value."""
        # Condition to show AC button over C | util para borrar y resetear los valores.
        return self.value in ("", "0", "0.0") and self.display == "0.0"

    def watch_show_ac(self, show_ac: bool) -> None:
        """When the show_ac attribute change we need to update the buttons."""
        # Show AC and hide C or vice versa
        self.c.visible = not show_ac
        self.ac.visible = show_ac


    def on_mount(self) -> None:
        # The calculator display
        # button : BIN -> B_2 , ...
        self.basedict = {10: 'DEC', 2: 'BIN', 8: 'OCT', 16: 'HEX', 32: '32bit', 64: '64bit'}
        self.textos = {base: EleganTexto(base,funcional=True,func_x=self.sel_base,bT = val) \
                       for val,base in self.basedict.items()}
        self.numbers = [Numbers() for i in range(4)] # ieee32,64 ->- ++ DECBINOCTHEX o [a,b],[u,v,...]
        self.ieee32num = Numbers()
        self.ieee64num = Numbers()

        self.bases = {10: False, 2: True, 8: False, 16: False, 32: False, 64: False}
        self.baseT = 2
        self.sel_base(10)


        self.exp32n = Numbers()
        self.exp64n = Numbers()
        self.mnt32dec = Numbers()
        self.mnt64dec = Numbers()


        self.titulo = EleganTexto(
            "Conversor de Bases: IEEE-754", "rgb(0,150,80) on rgb(20,20,20)")

        for i in range(len(self.numbers)):
            self.numbers[i].style_border = "bold"

        def make_button(text: str, style: str) -> Button:
            """Create a button with the given Figlet label."""
            return Button(FigletText(text), style=style, name=text)

        # Make all the buttons
            # Elegante compresion para formar botones
        self.buttons = {
            name: make_button(name, self.BUTTON_STYLES.get(name, self.DARK))
            for name in "+/-,D,E,F,A,B,C,7,8,9,4,5,6,1,2,3,.".split(",")
        }

        # Buttons that have to be treated specially
        self.zero = make_button("0", self.DARK)
        self.ac = make_button("AC", self.LIGHT)
        self.c = make_button("EC", self.YELLOW)
        self.elim  = make_button("DEL",self.LIGHT)
        self.c.visible = False

        # Set basic grid settingsq
        self.grid.set_gap(1, 1)
        self.grid.set_gutter(1)
        self.grid.set_align("center", "center")  # <- ?

        # Create rows / columns / areas
        self.grid.add_column("col", max_size=30, repeat=8) 
        self.grid.add_row("row", max_size=12, repeat=8)
        self.grid.add_areas(                     # <== if defined -> grid.place<->vincular
            clear="col1,row1",
            elim="col3,row1",
            texto10="col4,row2",
            texto2="col4,row3",
            texto8="col4,row4",
            texto16="col4,row5",
            titulo="col4-start|col8-end,row1",
            modo_32="col4,row6",
            modo_64="col4,row7",
            numbers10="col5-start|col8-end,row2",
            numbers2="col5-start|col8-end,row3",
            numbers8="col5-start|col8-end,row4",
            numbers16="col5-start|col8-end,row5",
            num_32='col5-start|col8-end,row6',
            num_64='col5-start|col8-end,row7',
            exp32t='col1,row8',
            exp64t='col4,row8',
            mnt32t='col2-start|col3-end,row8',
            mnt64t='col5-start|col8-end,row8',
            zero="col1-start|col2-end,row7",
        )  # Posicionamiento de areas en la grid
        # Place out widgets in to the layout
        # <- agrega el contenido a las areas definidas
        self.grid.place(clear=self.c)
        self.grid.place(
            numbers10=self.numbers[0],
            numbers2=self.numbers[1],
            numbers8=self.numbers[2],
            numbers16=self.numbers[3],
            texto10=self.textos['DEC'],
            texto2=self.textos['BIN'],
            texto8=self.textos['OCT'],
            texto16=self.textos['HEX'],
            modo_32=self.textos['32bit'],
            modo_64=self.textos['64bit'],
            titulo=self.titulo,
            elim=self.elim,
            num_32=self.ieee32num,
            num_64=self.ieee64num,
            exp32t=self.exp32n,
            exp64t=self.exp64n,
            mnt32t=self.mnt32dec,
            mnt64t=self.mnt64dec,
            *self.buttons.values(),
            clear=self.ac,
            zero=self.zero
        )
    
        '''  Para seleccionar en que base ingresar el número '''

    
    def sel_base(self, b) -> None:
        if b in (32, 64):
            self.modo_c = f'{b}bit'
        
        if b <=16:
            self.modo_c = 'estandar'

        act_style = "black on rgb(210,210,210)"
        dact_style = "yellow on rgb(20,40,20)"

        self.bases[self.baseT] = False
        self.textos[self.basedict[self.baseT]].style = dact_style
        
        self.bases[b] = True if not self.bases[b] else False
        self.textos[self.basedict[b]].style = act_style if self.bases[b] else dact_style
        if self.bases[b] == True:
            self.baseT = b if b <= 16 else 16
        else:
            self.baseT = 10
            self.bases[10] = True
            self.textos[self.basedict[10]].style = act_style
            self.modo_c = 'estandar'
        

        idx = self.getbaseT_idx()
        if idx != b and idx <= 3:
            self.value = self.numbers[idx].value
        
        if idx == 4:
            if self.value not in ('0.0', '0', ''):
                self.display = self.value = self.conversor.dec_ieee3264(self.numbers[0].value,mod=32)[0].replace(' ','')
                self.ieee32num.value = f'{self.value[0]} {self.value[1:10]} {self.value[10:]}'
        

        if idx == 5:
            if self.value not in ('0.0', '0', ''):
                self.display = self.value = self.conversor.dec_ieee3264(self.numbers[0].value, mod=64)[0].replace(' ','')
                self.ieee64num.value = f'{self.value[0]} {self.value[1:13]} {self.value[13:]}'
        
       


    def getbaseT_idx(self):
        idx : int = -1
        for i, x in enumerate(self.bases.values()):
            if x:
                idx = i
                break
        return idx
       


    def handle_button_pressed(self, message: ButtonPressed) -> None:
        """A message sent by the button widget
        Para darle funcionalidad a cada boton
        """

        assert isinstance(message.sender, Button)
        button_name = message.sender.name


        if button_name.isdigit():
            i = int(button_name)
            if (self.baseT == 8 and i > 7) \
            or ((self.baseT == 2 or self.modo_c != 'estandar') and i > 1) \
            or (self.modo_c != 'estandar' and len(self.value) >= int(self.modo_c[0:2])+1 ):
                pass
            else:
                self.display = self.value = self.value + button_name
            #self.display = self.value = self.value.lstrip("0") + button_name
        
        elif button_name == "+/-":
            if self.modo_c in ('32bit','64bit'):
                if self.ieee32num.value[0] == '0':
                    self.ieee32num.value[0] = '1'
                    self.ieee64num.value[0] = '1'
                elif self.ieee32num.value[0]== '1':
                    self.ieee32num.value[0] = '0'
                    self.ieee64num.value[0] = '0'

                self.display = self.value + ''
            elif self.modo_c == 'estandar':
                self.display = self.value = str(Decimal(self.value or '0') * -1)           
            self.display = self.value + ''

        elif button_name == "." and self.modo_c == 'estandar':  # importante para solo agregar un .
            if "." not in self.value:
                self.display = self.value = (self.value + '.' or "0.0")
        elif button_name == "AC":       # reset
            self.value = ""
            self.display = "0.0"

        elif button_name == "EC":
            self.value = ""
            self.display = "0.0"

        elif button_name in ('A','B','C','D','E','F') and self.modo_c == 'estandar':
            if self.baseT > 10:
                self.display = self.value = self.value.lstrip("0") + button_name

        elif button_name == "DEL":
            if len(self.value) > 0:
                self.display = self.value = self.value[0:len(self.value)-1]
            



class CalculatorApp(App):
    """The Calculator Pro V2.0 Application"""

    doc_size = 65
    calc = Calculator()
    bar : RenderableType

    async def on_load(self) -> None:
        await self.bind("g", "selectbase(10)", " DEC ")
        await self.bind("h", "selectbase(2)", " BIN ")
        await self.bind("j", "selectbase(8)", " OCT ")
        await self.bind("k", "selectbase(16)", "HEX ")
        await self.bind('n','act_ieee(32)','32bit')
        await self.bind('m', 'act_ieee(64)', '64bit')
        await self.bind("l", "act_docs", 'SRC')
        await self.bind("q", "quit", " Salir ")

    

    def action_act_ieee(self,modo) -> None:
        self.calc.sel_base(modo)
    

    def action_act_docs(self) -> None:
        self.bar.visible = not self.bar.visible
        self.calc.visible = not self.bar.visible

    def action_selectbase(self, b) -> None:
        self.calc.sel_base(b)
        
    def on_key(self, event):
        #idx = self.calc.getbaseT_idx()

        if event.key.isdigit():
            i = int(event.key)
            if (self.calc.baseT == 8 and i > 7) \
                or ((self.calc.baseT == 2 or self.calc.modo_c != 'estandar') and i > 1) \
                or (self.calc.baseT in (32, 64) and i > 1) \
                or (self.calc.modo_c != 'estandar' and len(self.calc.value) >= int(self.calc.modo_c[0:2])+1):
                pass
            else:
                self.calc.display = self.calc.value = self.calc.value + event.key
                #self.calc.numbers[idx].value = self.calc.display

        if self.calc.modo_c == 'estandar' and \
             event.key in ('a', 'b', 'c', 'd', 'e', 'f') or event.key in ('A','B','C','D','E','F'):
            if self.calc.baseT > 10 and self.calc.baseT < 17:
                self.calc.display = self.calc.value = self.calc.value + event.key.upper()
                #self.calc.numbers[idx].value = self.calc.display
        
        if event.key == '.':
            if self.calc.modo_c == 'estandar':
                if "." not in self.calc.display or self.display == '':
                    self.calc.display = self.calc.value = (self.calc.value + '.' or "0.0")
        
        if event.key == '-':
            if self.calc.modo_c == 'estandar':
                self.calc.display = self.calc.value = str(Decimal(self.calc.value or '0') * -1)
            elif self.calc.modo_c in ('32bit','64bit'):
                if self.calc.ieee32num.value[0] == '0':
                    self.calc.ieee32num.value = '1' + self.calc.ieee32num.value[1:]
                    self.calc.ieee64num.value = '1' + self.calc.ieee64num.value[1:]
                elif self.calc.ieee32num.value[0] == '1':
                    self.calc.ieee32num.value = '0' + self.calc.ieee32num.value[1:]
                    self.calc.ieee64num.value = '0' + self.calc.ieee64num.value[1:]


        
        if event.key == "ctrl+h": # === borrar (backspace)
            if self.calc.value != '':
                self.calc.display = self.calc.value = self.calc.value[0:len(self.calc.value)-1]


    async def on_mount(self) -> None:
        """Mount the calculator widget."""
        footer = Footer()
        self.bar = ScrollView(codigo_fuente,auto_width=True)
        self.bar.visible = False
     
        await self.view.dock(self.calc, edge='top')
        await self.view.dock(self.bar, edge='left', z=1)
        await self.view.dock(footer, edge='bottom', size=1, z=2)

        ##


ccs = Console()


def runApp():
    print(figlet_format("convbaspy", font="banner3-D"))
    print('''
    \n\t  David Penilla - Juan Camilo Bolaños - Santiago Abadía - Sergio Andrés Ángel - Jean Pierre Vargas
    \n\t----------------------------------------------------------------------------------------------------
    ''')
    ccs.print('\tAdvertencia:', style='red')
    print('\t   Intente no mantener presionada ninguna tecla.')
    ccs.print('\t   Presione en los resultados para copiar su valor.', style='green')
    input('\n\n - presione enter para continuar...')
    CalculatorApp.run(title="Calculadora IEEE754", log="textual.log")


runApp()