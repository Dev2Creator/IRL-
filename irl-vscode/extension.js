// IRL™ Language Support — run/build commands for .irl files.
// Copyright (C) 2026 Anika Mukherjee. AGPL-3.0-or-later.
const vscode = require('vscode');

function activeIrlFile() {
    const editor = vscode.window.activeTextEditor;
    if (!editor || !editor.document.fileName.endsWith('.irl')) {
        vscode.window.showInformationMessage('Open a .irl file first.');
        return null;
    }
    return editor.document.fileName;
}

function runInTerminal(command) {
    const terminal = vscode.window.createTerminal({ name: 'IRL™' });
    terminal.show();
    terminal.sendText(command);
}

function runFile() {
    const file = activeIrlFile();
    if (file) {
        runInTerminal(`irl "${file}"`);
    }
}

function buildFile() {
    const file = activeIrlFile();
    if (file) {
        runInTerminal(`irl lang build "${file}" -O2 -v`);
    }
}

function activate(context) {
    context.subscriptions.push(
        vscode.commands.registerCommand('irl-lang.runFile', runFile),
        vscode.commands.registerCommand('irl-lang.buildFile', buildFile)
    );
}

function deactivate() {}

module.exports = { activate, deactivate };
