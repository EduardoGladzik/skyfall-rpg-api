import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './style.css';
import Spells from '../spells.jsx';

export default function Home() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/magias" element={<Spells />} />
      </Routes>
    </BrowserRouter>
  );
}