
def convert_to(obj: object, new_dto_class):
    """
    Recebendo um objeto qualquer (parâmetro "obj"), e uma classe qualquer (parâmetro "new_dto_class"),
    este método cria uma instância da classe "new_dto_class", e copia todos os atributos do objeto
    "obj" para a nova instância, desde que haja um atributo com mesmo nome na classe de destino.
    """

    new_obj = new_dto_class()

    for attribute in obj.__dict__:
        attr_origem = getattr(obj, attribute, None)
        attr_destino = getattr(new_obj, attribute, None)

        # Pulando métodos
        if callable(attr_origem) or callable(attr_destino):
            continue

        setattr(new_obj, attribute, attr_origem)

    return new_obj
