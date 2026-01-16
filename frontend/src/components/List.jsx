import React, { useState, useEffect } from 'react';
import Item from './Item';

const List = () => {
    const [spells, setSpells] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchSpells();
    }, []);

    const fetchSpells = async () => {
        try {
            const response = await fetch('/api/magias');
            if (!response.ok) throw new Error('Erro ao buscar magias');
            const data = await response.json();
            setSpells(data);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    if (loading) return <div>Carregando...</div>;
    if (error) return <div>Erro: {error}</div>;

    return (
        <div className="spells-list">
            <h1>Spells</h1>
            <ul>
                {spells.map((spell) => (
                    <li key={spell.id || spell.name} className="spell-item">
                        <Item data={spell} />
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default List;