const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

async function contagemRegressiva() {
    console.log("Este programa faz uma contagem regressiva de 10 até 0");

    for (let i = 10; i >= 1; i--) {
        console.log(i);
        await sleep(1000);
    }
    console.log("FIM! 🎉🎉🎉🎉🎉🎉🎉🎉🎉");
}
contagemRegressiva();