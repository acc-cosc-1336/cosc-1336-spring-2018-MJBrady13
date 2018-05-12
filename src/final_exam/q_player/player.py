class Player:

    def check_come_out_roll(self, pas, d1, d2):

        if (d1 < 0 or d1 > 6) and (d2 < 0 or d2 > 6):

            return 'Invalid Range'

        elif d1 + d2 == 7 or d1 + d2 == 11:
            if pas:
                return 'Winner'
            else:
                return 'Loser'

        elif d1 + d2 == 2 or d1 + d2 == 3 or d1 + d2 == 12:
            if pas:
                return 'Loser'
            else:
                return 'Winner'
        else:

            return d1 + d2


