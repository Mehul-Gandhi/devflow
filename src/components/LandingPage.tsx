import React, { useState } from 'react';
import { Button, TextField, FormControl, InputLabel, Select, MenuItem } from '@mui/material';
const LandingPage: React.FC = () => {
    const [gitHubLink, setGitHubLink] = useState<string>('');
    const [mode, setMode] = useState<string>('question');
    const [prompt, setPrompt] = useState<string>('');

    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '40px' }}>
            <h1>Welcome to DevFlow</h1>
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
            />

            <FormControl variant="outlined" margin="normal" fullWidth>
                <InputLabel id="mode-label">Mode</InputLabel>
                <Select
                    labelId="mode-label"
                    id="mode-select"
                    value={mode}
                    onChange={(e) => setMode(e.target.value as string)}
                    label="Mode"
                >
                    <MenuItem value="question">Question</MenuItem>
                    <MenuItem value="flowchart">Flowchart</MenuItem>
                </Select>
            </FormControl>

            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="prompt"
                label={mode === 'question' ? 'Ask a Question' : 'Describe the Flowchart'}
                name="prompt"
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
            />

            <Button
                variant="contained"
                color="primary"
                style={{ marginTop: '20px' }}
                onClick={() => {
                    if (mode === 'question') {
                        // Handle question mode
                    } else {
                        // Handle flowchart mode
                    }
                }}
            >
                {mode === 'question' ? 'Ask Question' : 'Display Flowchart'}
            </Button>

            
        </div>
    );
}

export default LandingPage;
