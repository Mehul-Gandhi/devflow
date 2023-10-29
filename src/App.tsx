import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NotFound from "./components/NotFound"; 
import Convex  from "./convex";


function App() {
  return (
    <Router>
      {/* <NavBar /> */}
      <Routes>
        <Route index element={<Convex />} />
        <Route path="*" element={<NotFound />} />

      </Routes>
    </Router>
  )
  
}

export default App
