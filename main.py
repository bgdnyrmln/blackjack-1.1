from operator import ne
import sys
from deck import Koloda
from player import Player



class Game:
    def __init__(self):
        self.deck = Koloda()
        self.deck.generate()
        self.p = Player(False, self.deck)
        self.d = Player(True, self.deck)
    #spēles galvenais kods
    def play(self):
            print("Labi, lets go!")
            p_status = self.p.deal()
            d_status = self.d.deal()

            self.p.show()

            #čeko, vai useram ir blackjack uzreiz un pēc tam čeko dilleri
            if p_status == 1:
                print("Player saņema blackjack!")
                if d_status == 1:
                    print("Dilleris un player saņema blackjack!")
                #jautā, vai user grib vel vienu spēli
                cmd = ""
                while cmd != "jā":
                    print()
                    print("vel vienu reizi?(jā/nē)")
                    cmd = input("Atbilde: ")
                    if cmd == "nē" or cmd == "ne":
                        print("Goodbye!")
                        sys.exit()
                    elif cmd == "jā" or cmd == "ja":
                        print ("\n" * 100)
                        b = Game()
                        b.play()
            #jautā par hitu
            cmd = ""
            while cmd != "stop":
                bust = print("vel vai stop?")
                cmd = input("Atbilde: ")
                print()
                #hito un busta situācijā user looser
                if cmd == "vel":
                    bust = self.p.hit()
                    self.p.show()
                if bust == 1:
                    print("Player busted. ggwp!")
                    #jautā par vel vienu spēli
                    cmd = ""
                    while cmd != "jā":
                        print()
                        print("vel vienu reizi?(jā/nē)")
                        cmd = input("Atbilde: ")
                        if cmd == "nē" or cmd == "ne":
                            print("Goodbye!")
                            sys.exit()
                        elif cmd == "jā" or cmd == "ja":
                            print ("\n" * 100)
                            b = Game()
                            b.play()
            #čeko cai dillerim ir blackjack
            print("\n")
            self.d.show()
            if d_status == 1:
                print("Dillerim ir blackjack. Sorry bro, better luck next time!")
                #jautā par vel vienu spēli
                cmd = ""
                while cmd != "jā":
                    print()
                    print("vel vienu reizi?(jā/nē)")
                    cmd = input("Atbilde: ")
                    if cmd == "nē" or cmd == "ne":
                        print("Goodbye!")
                        sys.exit()
                    elif cmd == "jā" or cmd == "ja":
                        print ("\n" * 100)
                        b = Game()
                        b.play()
            #ja dillera score ir mazāks par 17 hito
            #busta situācijā dilleris looser
            while self.d.check_score() < 17:
                if self.d.hit() == 1:
                    self.d.show()
                    print("Dealer busted. Apsveicu!")
                    cmd = ""
                    while cmd != "jā":
                        print()
                        print("vel vienu reizi?(jā/nē)")
                        cmd = input("Atbilde: ")
                        if cmd == "nē" or cmd == "ne":
                            print("Goodbye!")
                            sys.exit()
                        elif cmd == "jā" or cmd == "ja":
                            print ("\n" * 100)
                            b = Game()
                            b.play()
                self.d.show()
            #salidzina usera un dillera summas
            if self.d.check_score() == self.p.check_score():
                print("1:1. Better luck next time!")
            elif self.d.check_score() > self.p.check_score():
                print("Dilleris uzvarēja. Good Game!")
            elif self.d.check_score() < self.p.check_score():
                print("Player uzvarēja. Apsveicu!")
            print()
            #jauta par vel vienu spēli
            cmd = ""
            while cmd != "jā":
                print()
                print("vel vienu reizi?(jā/nē)")
                cmd = input("Atbilde: ")
                if cmd == "nē" or cmd == "ne":
                    print("Goodbye!")
                    sys.exit()
                elif cmd == "jā" or cmd == "ja":
                    print ("\n" * 100)
                    b = Game()
                    b.play()

b = Game()
b.play()