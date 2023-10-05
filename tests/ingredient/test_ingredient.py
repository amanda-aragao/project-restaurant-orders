from src.models.ingredient import Ingredient, Restriction # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient('farinha')
    ingredient2 = Ingredient('farinha')
    ingredient3 = Ingredient('bacon')

    # verifica se name é o igual ao que foi passado no construtor
    assert ingredient1.name == 'farinha'

    # verifica se ao passar ingredientes iguais o hash é o mesmo
    assert hash(ingredient1) == hash('farinha')

    # Verifique se a representação em string é igual à esperada
    result_repr = "Ingredient('farinha')"
    assert repr(ingredient1) == result_repr

    # verifica se ao passar ingredientes iguais o resultado é true
    assert ingredient1.__eq__(ingredient2) is True

    # verifica se ao passar ingredientes diferentes o resultado é false
    assert ingredient1.__eq__(ingredient3) is False

    # Verifique se a restrição é um conjunto vazio
    ingredient3 = Ingredient('queijo mussarela')
    assert Restriction.LACTOSE in ingredient3.restrictions
    assert Restriction.ANIMAL_DERIVED in ingredient3.restrictions
