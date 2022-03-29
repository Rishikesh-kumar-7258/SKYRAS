import {Routes, Route} from 'react-router-dom'
import Home from './components/home.jsx';
import Login from './components/login.jsx';
import SchemePage from './components/schemepage.jsx';
import Profile from './components/profile.jsx';

function App() {
  return (
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="login" element={<Login/>}/>
        <Route path="/scheme" element={<SchemePage/>}/> 
        <Route path="/profile" element={<Profile/>}/>
      </Routes>
  );
}

export default App;
