import { Link } from 'react-router-dom';
import Button from '@mui/material/Button';
import HomeIcon from '@mui/icons-material/Home';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import styles from './styles/NotFound.module.css'; 

const NotFoundPage = () => {
  return (
    <div className={styles.container}>
    <div className="container text-center py-5">
      <h1 className="display-1">404</h1>
      <b>Page Not Found</b>
      <p className="lead">
        The page you are looking for might have been removed, had its name changed, or is temporarily unavailable.
      </p>
      <p>Please try the following:</p>
      <ul className="list-unstyled">
        <li>If you typed the page address in the Address bar, make sure that it is spelled correctly.</li>
        <li>
          Open the <Link to="/" className="text-decoration-none"><HomeIcon /> home page</Link>, and then look for links to the information you want.
        </li>
        <li>
          Click the <Button variant="outlined" startIcon={<ArrowBackIcon />} onClick={() => window.history.back()}>Back</Button> button to try another link.
        </li>
      </ul>
      <p className="mt-4">
        Or, you can just stay here and enjoy this cool coding visualization:
      </p>
        <img src="fibonacci.jpg" alt="Fibonacci"/>
    </div>
    </div>
  );
};

export default NotFoundPage;
