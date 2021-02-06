let brand = document.querySelector('.myBrand');

brand.addEventListener('click', () => {
    if (brand.innerHTML === 'Andrew Lorbieski') {
        brand.innerHTML = "Hey, Don't touch that!"
        brand.style.fontSize = '1.9em'
    } else {
        brand.innerHTML = 'Andrew Lorbieski'
        brand.style.fontSize = '2.2em'
    }
})