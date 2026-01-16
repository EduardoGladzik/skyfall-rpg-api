import React from 'react';

const Item = ({ data }) => {
    if (!data || typeof data !== 'object') {
        return <div className="item">Nenhum dado disponível</div>;
    }

    const fields = Object.keys(data);

    return (
        <div className="item">
            {fields.map((field) => (
                <div key={field} className="item-field">
                    <span className="item-label">{field}:</span>    
                    <span className="item-value">{String(data[field])}</span>
                </div>
            ))}
        </div>
    );
};

export default Item;