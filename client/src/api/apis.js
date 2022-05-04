// Get Businesses by City Name
const getBusinessesByCity = async (cityName) => {
    const response = await fetch(`http://127.0.0.1:5000/restaurants/${cityName}`)
    return response.json();
}

const apiServices = {
    getBusinessesByCity
}

export default apiServices