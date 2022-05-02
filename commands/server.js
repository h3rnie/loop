const { SlashCommandBuilder } = require("@discordjs/builders");

module.exports = {
    data: new SlashCommandBuilder()
        .setName("server")
        .setDescription("Comprehensive server information"),
    async execute(interaction) {
        let desc = "";
        if (interaction.guild.description) {
            desc = interaction.guild.description + "\n";
        }
        await interaction.reply(
            `${interaction.guild.name}\n${
                interaction.guild.memberCount
            } members\n${desc}${interaction.guild.preferredLocale}\n${
                interaction.guild.id
            }\n${interaction.guild.features}\n${interaction.guild.iconURL()}`
        );
    },
};
