import React from 'react';

const FormInput = (props) => {
    const { label, placeholder, type, onChange, name } = props;

    return (
        <div>
            <label>{label}</label>
            <input
                className="mt-2 mb-2 ml-5 mr-5 text-black"
                type={type}
                placeholder={placeholder}
                name={name}
                onChange={onChange}
            />
        </div>
    );
};

export default FormInput;
