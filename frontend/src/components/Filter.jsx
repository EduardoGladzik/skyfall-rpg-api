import React, { useState } from 'react';

export default function Filter({ onFilter }) {
    const [filters, setFilters] = useState({
        name: '',
        cost: '',
        layer: '',
        descriptor: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFilters(prev => ({
            ...prev,
            [name]: value
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onFilter(filters);
    };

    const handleReset = () => {
        setFilters({
            name: '',
            cost: '',
            layer: '',
            descriptor: ''
        });
        onFilter({
            name: '',
            cost: '',
            layer: '',
            descriptor: ''
        });
    };

    return (
        <form onSubmit={handleSubmit} className="filter-container">
            <input
                type="text"
                name="name"
                placeholder="Filtrar por nome"
                value={filters.name}
                onChange={handleChange}
            />
            
            <input
                type="text"
                name="cost"
                placeholder="Filtrar por custo"
                value={filters.cost}
                onChange={handleChange}
            />
            
            <input
                type="text"
                name="layer"
                placeholder="Filtrar por camada"
                value={filters.layer}
                onChange={handleChange}
            />
            
            <input
                type="text"
                name="descriptor"
                placeholder="Filtrar por descritor"
                value={filters.descriptor}
                onChange={handleChange}
            />
            
            <button type="submit">Filtrar</button>
            <button type="button" onClick={handleReset}>Limpar</button>
        </form>
    );
}