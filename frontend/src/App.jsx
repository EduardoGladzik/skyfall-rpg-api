import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Spells from './pages/spells';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Spells />} />
        <Route path="/spells" element={<Spells />} />
      </Routes>
    </BrowserRouter>
  );
}