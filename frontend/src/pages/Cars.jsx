import Layout from '../components/Layout'
import Card from '../components/Card'
import {useState, useEffect} from 'react'


const Cars = () => {
    const [cars, setCars] = useState([])
    const [brand, setBrand] = useState('')
    const [minPrice, setMinPrice] = useState(0)
    const [maxPrice, setMaxPrice] = useState(50000)
    const [isPending, setIsPending] = useState(true)

    // fetch all cars initially
    useEffect(() => {
        fetch(`http://localhost:8000/cars?brand=${brand}&min_price=${minPrice}&max_price=${maxPrice}`)
            .then(response => response.json())
            .then(json => setCars(json))
            setIsPending(false)
    }, [brand, minPrice, maxPrice])

    const handleChangeBrand = (event) => {
        setCars([])
        setBrand(event.target.value)
        setIsPending(true)
    }

    const handleChangeMinPrice = (event) => {
        setCars([])
        setMinPrice(event.target.value)
        setIsPending(true)
    }

    const handleChangeMaxPrice = (event) => {
        setCars([])
        setMaxPrice(event.target.value)
        setIsPending(true)
    }

    return (
        <Layout>
            <div className='flex flex-row'>
                <div className='m-3'>
                    <label htmlFor="cars" className='text-white m-5'>
                        Choose a brand: 
                    </label>
                    <select name="cars" id="cars" onChange={handleChangeBrand}>
                        <option value="">All cars</option>
                        <option value="Fiat">Fiat</option>
                        <option value="Ford">Ford</option>
                    </select>
                </div>
                <div className='m-3'>
                    <label htmlFor="min-price" className='text-white m-5'>
                        Minimum Price: 
                    </label>
                    <input type="range" id="min-price" min="0" max="49999" value={minPrice} onChange={handleChangeMinPrice} />
                    <span className='text-white ml-2'>{minPrice}</span>
                </div>
                <div className='m-3'>
                    <label htmlFor="max-price" className='text-white m-5'>
                        Maximum Price: 
                    </label>
                    <input type="range" id="max-price" min="1" max="50000" value={maxPrice} onChange={handleChangeMaxPrice} />
                    <span className='text-white ml-2'>{maxPrice}</span>
                </div>
            </div>


            <div>
                {
                isPending && <div><h2 className='text-white'>Loading cars, brand: {brand}...</h2></div>                   
                }
                <div className='flex flex-wrap'>
                    {
                        cars && cars.map(
                            (el) => {
                                return (
                                    <Card key={el._id} car = {el} />
                                )
                            }
                        )
                    }
                </div>
            </div>
        </Layout>
    )
}

export default Cars