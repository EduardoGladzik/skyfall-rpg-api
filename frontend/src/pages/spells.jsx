import { useEffect, useState } from 'react';

function SpellsPage() {
    // 1. Criamos a "memória" para as magias. Começa como uma lista vazia [].
    const [spells, setSpells] = useState([]);
    
    // 2. Criamos um estado para saber se a API ainda está processando.
    const [loading, setLoading] = useState(true);

    // 3. O "Gatilho" que roda quando a página abre.
    useEffect(() => {
        // Função assíncrona para buscar os dados
        const fetchSpells = async () => {
            try {
                const response = await fetch('http://localhost:8000/api/spells/');
                const data = await response.json();
                
                // Guardamos o resultado do Django na nossa memória 'spells'
                setSpells(data);
                setLoading(false);
            } catch (error) {
                console.error("Erro ao buscar magias:", error);
                setLoading(false);
            }
        };

        fetchSpells();
    }, []); // Este [] vazio garante que a busca só ocorra UMA vez.

    // 4. Lógica de exibição (O que o usuário vê)
    if (loading) return <p>Carregando...</p>;

    return (
        <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
            <h1>Catálogo de Magias - Skyfall</h1>
            
            <div style={{ display: 'grid', gap: '20px' }}>
                {spells.map((spell) => (
                    <div key={spell.id} style={{
                        border: '1px solid #ddd',
                        padding: '15px',
                        borderRadius: '8px',
                        backgroundColor: '#f9f9f9'
                    }}>
                        <h2 style={{ color: '#2c3e50' }}>{spell.name}</h2>
                        <p><strong>Custo:</strong> {spell.cost} PM</p>
                        <p><strong>Execução:</strong> {spell.execution_type}</p>
                        <p>{spell.description}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default SpellsPage;