const { SlashCommandBuilder } = require("@discordjs/builders");

module.exports = {
    data: new SlashCommandBuilder()
        .setName("shards")
        .setDescription("WebSocket Shard Connection"),
    async execute(interaction) {
        const sock = interaction.client.ws;
        const ls = [
            "ready",
            "connecting",
            "disconnecting",
            "idle",
            "nearly",
            "disconnected",
            "waiting for guilds",
            "identifying",
            "resuming",
        ];
        let status = ls[sock.status];
        let no = "s";
        if (sock.shards.size == 1) {
            no = "";
        }
        await interaction.reply({
            content: `${sock.shards.size} shard${no} currently ${status} through ${sock.gateway}`,
            ephemeral: true,
        });
    },
};
