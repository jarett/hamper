from hamper.interfaces import Command, ChatCommandPlugin


class ChannelUtils(ChatCommandPlugin):

    name = 'channelutils'
    priority = 0

    class JoinCommand(Command):
        regex = r'^join (.*)$'

        def command(self, bot, comm, groups):
            """Join a channel, and say you did."""
            chan = groups[0]
            if not chan.startswith('#'):
                chan = '#' + chan
            bot.join(chan)
            bot.reply(comm, 'OK, {0}.'.format(comm['user']))

        def process(self, bot, comm):
            if self.onlyDirected and not comm['directed']:
                return
            match = self.regex.match(comm['message'])
            print "JoinCommand match={0}".format(match)
            if match:
                self.command(bot, comm, match.groups())
                return True

    class LeaveCommand(Command):
        regex = r'^leave (#?[-_a-zA-Z0-9])?$'

        def command(self, bot, comm, groups):
            """Join a channel, and say you did."""
            chan = groups[0]
            if chan is None:
                chan = comm['channel']
            if not chan.startswith('#'):
                chan = '#' + chan
            bot.reply(comm, 'Bye!')
            bot.leave(chan)


channel_utils = ChannelUtils()
