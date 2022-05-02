const Statcord = require("statcord.js");

module.exports = {
    name: "ready",
    once: false,
    execute(client) {
        const statcord = new Statcord.Client({
            client,
            key: process.env.STATCORD,
            postCpuStatistics: true,
            postMemStatistics: true,
            postNetworkStatistics: true,
        });
        console.log(`Ready! Logged in as ${client.user.tag}`);
        statcord.autopost();
    },
};
