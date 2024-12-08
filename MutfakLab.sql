CREATE TABLE recipes ( -- dummy table oluşturma kısmı
    id INT PRIMARY KEY,
    name VARCHAR(200),
    ingredients JSON
);


INSERT INTO recipes (id, name, ingredients) -- değer ekle
VALUES 
(1, 'Domates Çorbası', JSON_ARRAY('Domates', 'Kaşar', 'Tereyağı')),
(2, 'Cacık', JSON_ARRAY('Sarımsak', 'Yoğurt')),
(3, 'Domatesli Mücver', JSON_ARRAY('Domates', 'Kabak', 'Tereyağı'));


SET @user_input = JSON_ARRAY('Domates'); -- inputu ayarla

SELECT name -- where the magic happens
FROM recipes AS r
WHERE NOT EXISTS (
    SELECT 1
    FROM JSON_TABLE(r.ingredients, '$[*]' COLUMNS(ingredient VARCHAR(50) PATH '$')) AS recipe_ingredients
    WHERE recipe_ingredients.ingredient NOT IN (
        SELECT user_input_values.value
        FROM JSON_TABLE(@user_input, '$[*]' COLUMNS(value VARCHAR(50) PATH '$')) AS user_input_values
    )
);
