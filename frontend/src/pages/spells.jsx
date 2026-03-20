import { useEffect, useState } from 'react';
import logoImg from '../assets/logo.png';

function SpellsPage() {
    const [spells, setSpells] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [searchTerm, setSearchTerm] = useState('');

    return (
        <div className="min-h-screen bg-[#0f111a] text-gray-200 font sans">
            {/* Navbar */}
            <nav className="bg-gray-900 border-b border-gray-800 px-6 py-4 flex justify-between items-center">
                {/* Título e Logo */}
                <div className="flex items-center gap-3">
                    <img src={logoImg} alt="Logo" className="h-8 object-contain" />
                    <span className="text-xl font-bold text-purple-400 tracking-wider">Skyfall RPG API</span>
                </div>
                {/* Links de Navegação */}
                <div className='hidden md:flex gap-6 text-sm font-medium text-gray-400'>
                    <a href="#" className="hover:text-purple-400 transition-colors">Magias</a>
                    <a href="#" className="hover:text-purple-400 transition-colors duration-300">Classes</a>
                    <a href="#" className="hover:text-purple-400 transition-colors duration-300">Trilhas</a>
                    <a href="#" className="hover:text-purple-400 transition-colors duration-300">Legados</a>
                </div>
            </nav>
        </div>
    )
}
export default SpellsPage;