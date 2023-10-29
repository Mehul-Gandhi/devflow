import React from 'react';
import './LandingPage.css';

const LandingPage: React.FC = () => {
    return (
        <div className="container">
            <header className="header">
                <h1>GitHub Helper</h1>
            </header>
            <main className="main-content">
                <h2>Welcome to GitHub Helper</h2>
                <p>Ask questions about any GitHub repo or visualize its structure.</p>
                <input type="text" placeholder="Enter GitHub repo link" />
                <button>Submit</button>
            </main>
            <footer className="footer">
                <p>© 2023 GitHub Helper</p>
            </footer>
        </div>
    );
}

export default LandingPage;