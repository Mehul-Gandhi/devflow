import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NotFound from "./components/NotFound"; 
import LandingPage from "./components/LandingPage";
import Convex  from "./convex";


function App() {
  return (
    <Router>
      {/* <NavBar /> */}
      <Routes>
        <Route index element={<LandingPage />} />
        <Route path="/convex" element={<Convex />} />
        <Route path="*" element={<NotFound />} />

      </Routes>
    </Router>
  )
  
}

export default App
