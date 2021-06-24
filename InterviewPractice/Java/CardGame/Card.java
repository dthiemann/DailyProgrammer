package InterviewPractice.Java.CardGame;

/**
 * Class representing a classic playing card
 */
public class Card {
    private Suit suit;
    private int faceValue; // Jack (11), Queen (12), King (13), Ace (1)

    public int getFaceValue() {
        return this.faceValue;
    }

    public Suit getSuit() {
        return this.suit;
    }
}
