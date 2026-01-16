import React from 'react';
import Header from '../components/Header';
import Filter from '../components/Filter';
import List from '../components/List';

const Spells = () => {
    const handleFilter = (filters) => {
    };

    return (
        <div className="spells-page">
            <Header />
            <Filter onFilter={handleFilter} />
            <List />
        </div>
    );
};

export default Spells;