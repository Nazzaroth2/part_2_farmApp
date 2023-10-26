import React from 'react';
import { Link } from 'react-router-dom';

const Card = (props) => {
    return (
        <Link to={'/cars/'+props.car._id} className='block'>
            <div className="w-60 overflow-auto bg-gray-800 border border-blue-400 rounded-lg m-4 p-4 shadow-lg transform transition-transform hover:scale-105">
                <h2 className="text-blue-400 font-bold text-lg mb-2">
                    {props.car.brand}
                </h2>
                <p className="text-white mb-1">
                    <strong>Model:</strong> {props.car.model}
                </p>
                <p className="text-white mb-1">
                    <strong>Year:</strong> {props.car.year}
                </p>
                <p className="text-contrast mb-1">
                    <strong>Price: {props.car.price}</strong>
                </p>
                <p className="text-white mb-1">
                    <strong>Km:</strong> {props.car.km}
                </p>
                <p className="text-white mb-1">
                    <strong>Engine:</strong> {props.car.cm3}cm3
                </p>
            </div>
        </Link>
    );
};

export default Card;
