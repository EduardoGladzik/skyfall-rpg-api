import { useEffect, useState } from 'react';
import axios from 'axios';

function SpellsPage() {
    // Gerenciamento de Estado
    const [spells, setSpells] = useState([]); // Guarda a lista de magias
    const [loading, setLoading] = useState(true); // Controla o status de carregamento
    const [searchTerm, setSearchTerm] = useState(''); // Guarda o texto digitado na busca

    // Busca os dados da API quando a página carrega
    useEffect(() => {
        const fetchSpells = async () => {
            try {
                const response = await axios.get('/api/magias');
                setSpells(response.data);
            } catch (error) {
                console.error("Erro ao buscar magias:", error);
            } finally {
                setLoading(false); 
            }
        };

        fetchSpells();
    }, []);

    // Filtra as magias em tempo real com base no texto de busca
    const filteredSpells = spells.filter(spell =>
        spell.name.toLowerCase().includes(searchTerm.toLowerCase())
    );

    // Cabeçalho e Filtros
    return (
        <div className="min-h-screen bg-[#0e0f15] text-gray-200 font-sans p-8">
            
            {/* --- CABEÇALHO --- */}
            <header className="relative mb-10 pb-6 flex flex-col md:flex-row justify-between items-start md:items-end gap-4">
                <div>
                    <h1 className="text-4xl md:text-5xl font-serif font-bold text-white mb-2 tracking-wider">MAGIAS</h1>
                    <div className="h-1 w-24 bg-yellow-500 rounded-full"></div>
                </div>
                
                <div className="flex gap-4 text-sm font-medium">
                    <button className="px-5 py-2.5 border border-gray-600 rounded flex items-center gap-2 hover:bg-gray-800 transition-colors cursor-pointer">
                        Regras de Magia
                    </button>
                    <button className="px-5 py-2.5 bg-[#f5b83d] text-black rounded flex items-center gap-2 hover:bg-yellow-400 transition-colors cursor-pointer font-bold">
                        Criar Magia
                    </button>
                </div>
            </header>

            {/* --- SEÇÃO DE FILTROS --- */}
            <div className="bg-[#171821] p-6 rounded-lg mb-6 shadow-lg border border-gray-800">
                <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
                    
                    {/* Input de Busca (Conectado ao Estado) */}
                    <div className="flex flex-col gap-2">
                        <label className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Nome da Magia</label>
                        <input 
                            type="text" 
                            placeholder="Buscar magias..." 
                            className="w-full bg-[#1e202d] border border-gray-700 rounded py-2 px-4 focus:outline-none focus:border-yellow-500 transition-colors"
                            value={searchTerm} // O valor exibido é o que está no estado
                            onChange={(e) => setSearchTerm(e.target.value)} // Atualiza o estado quando digitamos
                        />
                    </div>

                    {/* Menus Suspensos (Visuais por enquanto) */}
                    <div className="flex flex-col gap-2">
                        <label className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Classe</label>
                        <select className="w-full bg-[#1e202d] border border-gray-700 rounded py-2.5 px-4 appearance-none focus:outline-none focus:border-yellow-500 text-gray-300">
                            <option>Todos</option>
                        </select>
                    </div>
                    <div className="flex flex-col gap-2">
                        <label className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Camada (Nível)</label>
                        <select className="w-full bg-[#1e202d] border border-gray-700 rounded py-2.5 px-4 appearance-none focus:outline-none focus:border-yellow-500 text-gray-300">
                            <option>Todos</option>
                        </select>
                    </div>
                    <div className="flex flex-col gap-2">
                        <label className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Escola</label>
                        <select className="w-full bg-[#1e202d] border border-gray-700 rounded py-2.5 px-4 appearance-none focus:outline-none focus:border-yellow-500 text-gray-300">
                            <option>Todos</option>
                        </select>
                    </div>
                    <div className="flex flex-col gap-2">
                        <label className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Tempo de Conjuração</label>
                        <select className="w-full bg-[#1e202d] border border-gray-700 rounded py-2.5 px-4 appearance-none focus:outline-none focus:border-yellow-500 text-gray-300">
                            <option>Todos</option>
                        </select>
                    </div>
                </div>
            </div>

            {/* --- CONTADOR DE RESULTADOS --- */}
            <p className="text-gray-400 mb-4 text-sm font-medium">
                {filteredSpells.length} magias encontradas
            </p>

            {/* --- TABELA DE RESULTADOS --- */}
            <div className="bg-[#171821] rounded-lg overflow-x-auto border border-gray-800 shadow-lg">
                <table className="w-full text-left border-collapse min-w-[800px]">
                    
                    {/* Cabeçalho da Tabela */}
                    <thead className="bg-[#1c1e29] border-b border-gray-800 text-xs font-semibold text-gray-400 uppercase tracking-wider">
                        <tr>
                            <th className="py-4 px-6 font-medium">Camada<span className="text-gray-600 ml-1">↑↓</span></th>
                            <th className="py-4 px-6 font-medium">Nome<span className="text-gray-600 ml-1">↑↓</span></th>
                            <th className="py-4 px-6 font-medium">Custo (PE)<span className="text-gray-600 ml-1">↑↓</span></th>
                            <th className="py-4 px-6 font-medium">Conjuração<span className="text-gray-600 ml-1">↑↓</span></th>
                            <th className="py-4 px-6 font-medium">Descritores</th>
                            <th className="py-4 px-6 font-medium">Alcance<span className="text-gray-600 ml-1">↑↓</span></th>
                            <th className="py-4 px-6 font-medium">Duração<span className="text-gray-600 ml-1">↑↓</span></th>
                        </tr>
                    </thead>
                    
                    {/* Corpo da Tabela */}
                    <tbody className="text-sm">
                        {/* 1. Verifica se está carregando */}
                        {loading ? (
                            <tr>
                                <td colSpan="6" className="py-8 text-center text-gray-500">
                                    Buscando magias nos grimórios...
                                </td>
                            </tr>
                        ) : filteredSpells.length > 0 ? (
                            /* 2. Se não está carregando e tem magias, faz o "map" para criar as linhas */
                            filteredSpells.map((spell) => (
                                <tr key={spell.id} className="border-b border-gray-800/50 hover:bg-[#1e202d] transition-colors">
                                    <td className="py-4 px-6 flex items-center gap-2 font-medium">
                                        <span className="text-red-400">✧</span> {spell.layer}
                                    </td>
                                    <td className="py-4 px-6">
                                        <div className="font-bold text-gray-100 text-base">{spell.name}</div>
                                        <div className="text-xs text-gray-500 mt-0.5">
                                            {spell.category} • {spell.components.join(', ')}
                                        </div>
                                    </td>
                                    <td className="py-4 px-6 text-gray-300">{spell.cost < 0 ? spell.cost : spell.cost + ' PE'}</td>
                                    <td className="py-4 px-6 text-gray-300">{spell.execution_type}</td>
                                    <td className="py-4 px-6 text-gray-300">{spell.descriptors.join(', ')}</td>
                                    <td className="py-4 px-6 text-gray-300">
                                        {spell.range > 0 ? `${spell.range}m` : 'Toque'}
                                    </td>
                                    <td className="py-4 px-6 text-gray-300">
                                        {spell.duration}
                                    </td>
                                </tr>
                            ))
                        ) : (
                            /* 3. Se não está carregando, mas a busca não encontrou nada */
                            <tr>
                                <td colSpan="6" className="py-8 text-center text-gray-500">
                                    Nenhuma magia encontrada com o nome "{searchTerm}".
                                </td>
                            </tr>
                        )}
                    </tbody>
                </table>
            </div>
            
        </div>
    );
}

export default SpellsPage;