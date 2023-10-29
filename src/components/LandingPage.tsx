import React, { useState } from 'react';
import { Button, TextField, FormControl, InputLabel, Select, MenuItem, InputAdornment  } from '@mui/material';
import { Radio, RadioGroup, FormControlLabel } from '@mui/material';

import styles from "./styles/LandingPage.module.css";

const LandingPage: React.FC = () => {
    const [gitHubLink, setGitHubLink] = useState<string>('');
    const [mode, setMode] = useState<string>('question');
    const [prompt, setPrompt] = useState<string>('');

    return (
<div style={{ 
    display: 'flex', 
    flexDirection: 'column', 
    alignItems: 'center', 
    padding: '40px', 
}}>          <h1>Welcome to DevFlow</h1>
            <p>
                Empowering new engineers with the tools and insights to understand the codebase faster than ever. Dive deep, ask questions, visualize structures - all in one place.
            </p>

            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="githubLink"
                label="Enter GitHub Link"
                name="githubLink"
                autoFocus
                value={gitHubLink}
                onChange={(e) => setGitHubLink(e.target.value)}
                placeholder="https://github.com/pioneers/shepherd"

            />

<RadioGroup 
    row 
    value={mode} 
    onChange={(e) => setMode(e.target.value)}>
    <FormControlLabel 
        value="question" 
        control={<Radio color="primary" />} 
        label="Question" 
    />
    <FormControlLabel 
        value="flowchart" 
        control={<Radio color="primary" />} 
        label="Flowchart" 
    />
</RadioGroup>



            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="prompt"
                label={mode === 'question' ? 'Ask a Question' : 'Describe the Desired Flowchart'}
                name="prompt"
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
            />
            
            <Button
                variant="contained"
                color="primary"
                style={{ marginTop: '20px' }}
                onClick={() => {
                    // Handle the action here
                }}
            >
                Submit
            </Button>
            
        </div>
    );
}

export default LandingPage;
