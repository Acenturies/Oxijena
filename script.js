/*
   Copyright 2024 Acenturies

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
document.addEventListener('DOMContentLoaded', () => {
    const commandInput = document.getElementById('commandInput');
    const output = document.getElementById('output');
    const prompt = document.getElementById('prompt');
    output.innerHTML += `<div>Welcome To Oxijena 1.0.0 Alpha 1 (Heavily Unfinished), For Help Please Execute The Command 'help'`;
    const commandHistory = [];
    let historyIndex = -1;

    commandInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            const command = commandInput.value.trim();
            if (command) {
                commandHistory.push(command);
                historyIndex = -1;
                processCommand(command);
                commandInput.value = '';
            }
        } else if (event.key === 'ArrowUp') {
            if (historyIndex < commandHistory.length - 1) {
                historyIndex++;
                commandInput.value = commandHistory[commandHistory.length - 1 - historyIndex];
            }
        } else if (event.key === 'ArrowDown') {
            if (historyIndex > 0) {
                historyIndex--;
                commandInput.value = commandHistory[commandHistory.length - 1 - historyIndex];
            } else {
                historyIndex = -1;
                commandInput.value = '';
            }
        }
    });

    function processCommand(command) {
        // Display the command in the output
        output.innerHTML += `<div>${prompt.innerHTML} ${command}</div>`;

        // Process command (you can add more commands here)
        switch (command.toLowerCase()) {
            case 'time':
                output.innerHTML += `<div>Time Unfinished</div>`;
                break;
            case 'clear':
                output.innerHTML = '';
                break;
            case 'version':
                output.innerHTML += `<div>Oxijena Terminal, Version 1.0.0</div>`;
                break;
            case 'help':
                output.innerHTML += `<div>[version] shows the version</div>`;
                output.innerHTML += `<div>[time] shows the time</div>`;
                output.innerHTML += `<div>[help] shows help</div>`;
                output.innerHTML += `<div>[colour]('help color' for more info) changes the color to red</div>`;
                break;
            case 'color 1':
                var line = document.getElementById("inputlineclass");
                line.classList.toggle("input-line-1");
                var body = document.getElementById("body");
                body.classList.toggle("color1");
                break;
            case 'color 2':
                var line = document.getElementById("inputlineclass");
                line.classList.toggle("input-line-2");
                var body = document.getElementById("body");
                body.classList.toggle("color2");
                break;
            case 'color 3':
                var line = document.getElementById("inputlineclass");
                line.classList.toggle("input-line-3");
                var body = document.getElementById("body");
                body.classList.toggle("color3");
                break;
            case 'color 4':
                var line = document.getElementById("inputlineclass");
                line.classList.toggle("input-line-4");
                var body = document.getElementById("body");
                body.classList.toggle("color4");
                break;
            case 'color 5':
                var line = document.getElementById("inputlineclass");
                line.classList.toggle("input-line-5");
                var body = document.getElementById("body");
                body.classList.toggle("color5");
                break;
            default:
                output.innerHTML += `<div>Command not recognized: ${command}</div>`;
                break;
            
        }

        // Scroll to the bottom
        output.scrollTop = output.scrollHeight;
    }
});
