const debug = false;

function logDebug(message) {
    if (debug) {
        console.log(message);
    }
}

function sendNowPlaying() {
    logDebug('sendNowPlaying function called.');
    const songElement = document.querySelector('.title.style-scope.ytmusic-player-bar');
    const artistElement = document.querySelector('.subtitle.ytmusic-player-bar > yt-formatted-string > a');
    const albumArtElement = document.querySelector('.image.style-scope.ytmusic-player-bar');

    if (!songElement || !artistElement) {
        logDebug('No music playing. Not sending any data.');
        return;
    }

    const song = songElement.textContent.trim();
    const artist = artistElement.textContent.trim();
    const albumArt = albumArtElement ? albumArtElement.src : '';

    logDebug(`Song: ${song}`);
    logDebug(`Artist: ${artist}`);
    logDebug(`Album Art: ${albumArt}`);

    fetch('http://localhost:5000/update', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ song, artist, albumArt })
    })
    .then(response => response.json())
    .then(data => logDebug(`Response from server: ${JSON.stringify(data)}`))
    .catch(error => logDebug(`Error: ${error}`));
}

// Debounce function
function debounce(func, wait) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
}

// Debounced version of sendNowPlaying
const debouncedSendNowPlaying = debounce(sendNowPlaying, 100);

const targetNode = document.querySelector('ytmusic-player-bar');
const config = { childList: true, subtree: true };

const callback = function(mutationsList, observer) {
    for (let mutation of mutationsList) {
        if (mutation.type === 'childList') {
            debouncedSendNowPlaying();
        }
    }
};

const observer = new MutationObserver(callback);

if (targetNode) {
    observer.observe(targetNode, config);
    logDebug('MutationObserver is set.');
} else {
    logDebug('ytmusic-player-bar element not found.');
}
