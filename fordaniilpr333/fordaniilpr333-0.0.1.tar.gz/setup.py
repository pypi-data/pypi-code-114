# Импорт недавно установленного пакета setuptools.
import setuptools




# Определение requests как requirements для того, чтобы этот пакет работал. Зависимости проекта.
# requirements = ["requests<=2.21.0"]

# Функция, которая принимает несколько аргументов. Она присваивает эти значения пакету.
setuptools.setup(
	# Имя дистрибутива пакета. Оно должно быть уникальным, поэтому добавление вашего имени пользователя в конце является обычным делом.
	name="fordaniilpr333",
	# Номер версии вашего пакета. Обычно используется семантическое управление версиями.
	version="0.0.1",
	# Имя автора.
	author="Daniil Ruzhkov",
	# Его почта.
	author_email="d.ruzhkov7@gmail.com",
	# Краткое описание, которое будет показано на странице PyPi.
	description="My package1",

	# URL-адрес, представляющий домашнюю страницу проекта. Большинство проектов ссылаются на репозиторий.
	url="https://github.com/ericjaychi/sample-pypi-package",
	# Находит все пакеты внутри проекта и объединяет их в дистрибутив.
	packages=setuptools.find_packages(),
	# requirements или dependencies, которые будут установлены вместе с пакетом, когда пользователь установит его через pip.
	# install_requires=requirements,
	# Предоставляет pip некоторые метаданные о пакете. Также отображается на странице PyPi.
	classifiers=[
		"Programming Language :: Python :: 3.8",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	# Требуемая версия Python.
	python_requires='>=3.6',
)