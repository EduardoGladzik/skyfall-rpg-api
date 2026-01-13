import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [habilidades, setHabilidades] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Tenta buscar as habilidades no teu Django
    axios.get('http://127.0.0.1:8000/api/habilidades')
      .then(response => {
        setHabilidades(response.data)
        setLoading(false)
      })
      .catch(error => {
        console.error("Erro ao buscar dados:", error)
        setLoading(false)
      })
  }, [])

  return (
    <div className="container">
      <h1>Compêndio Skyfall RPG</h1>
      
      {loading ? (
        <p>A carregar grimório...</p>
      ) : (
        <div className="lista-cards">
          {habilidades.map((ability) => (
            <div key={ability.name} className="card">
              <div className="card-header">
                <h2>{ability.name}</h2>
                <span className="custo">{ability.cost} PE</span>
              </div>
              
              <div className="tags">
                <span className="tag">{ability.execution_type}</span>
                <span className="tag">{ability.duration}</span>
              </div>

              <div className="descricao">
                <p>{ability.description}</p>
                {/* Mostra efeito se existir */}
                {ability.effect && (
                    <p><strong>Efeito:</strong> {ability.effect}</p>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default App