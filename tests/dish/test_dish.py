import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 2
def test_dish():
    # Teste de inicialização do nome do prato

    dish1 = Dish("Lasanha", 24.99)
    dish2 = Dish("Ravioli com bacon", 34.99)
    dish3 = Dish("Ravioli com bacon", 34.99)

    assert dish1.name == "Lasanha"

    # Teste de igualdade de pratos
    dish2 = Dish("Ravioli com bacon", 34.99)
    dish3 = Dish("Ravioli com bacon", 34.99)
    assert dish2 == dish3

    # verifica se ao passar pratos iguais o hash é o mesmo
    assert hash(dish2) == hash(dish3)

    # verifica se ao passar pratos diferentes o hash é o mesmo
    assert hash(dish1) != hash(dish2)
    assert hash(dish1) == hash(Dish("Lasanha", 24.99))

    # Verifique se a representação em string é igual à esperada
    result_repr = "Dish('Ravioli com bacon', R$34.99)"
    assert repr(dish2) == result_repr

    # Teste para adicionar ingredientes ao prato
    ingredient1 = Ingredient("massa de ravioli")
    ingredient2 = Ingredient("bacon")
    dish3.add_ingredient_dependency(ingredient1, 2)
    dish3.add_ingredient_dependency(ingredient2, 4)

    # Verifique se as restrições do prato estão corretas

    assert dish3.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.GLUTEN,
        Restriction.LACTOSE,
    }

    # verifica se ao passar pratos iguais o resultado é true
    assert dish2.__eq__(dish3) is True

    # verifica se ao passar pratos diferentes o resultado é false
    assert dish1.__eq__(dish2) is False

    # verifica função get_ingredients do prato
    assert dish3.get_ingredients() == {
        Ingredient("massa de ravioli"), Ingredient("bacon")}

    # verifica TypeError ao passar atributo (preço) do prato diferente de int
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Ravioli com bacon", "34.99")

    # Teste de erro de valor (preço menor ou igual a zero)
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Ravioli com bacon", -1.0)
