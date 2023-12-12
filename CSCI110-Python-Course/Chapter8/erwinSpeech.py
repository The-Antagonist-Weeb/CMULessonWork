#-------------------------------------------------------------------
# Written by Carter Stickler, December 2023.
#
# Anyone may freely copy or modify this program. 
#   Assuming you can find it in my hidden github. 
#   Or if you're the instructor, and I wound up handing this to you.
#-------------------------------------------------------------------
import string

erwinsSpeech = """
It's all meaningless. No matter what dreams or hopes you had. No matter how blessed a life you've lived. It's all the same if you're shredded by rocks. Everyone will die someday. Does that mean life is meaningless? Was there even any meaning in us being born? Would you say that of our fallen comrades? Their lives...were they meaningless?
No, they weren't! It's us who gives meaning to our comrade's lives! The brave fallen! The anguished fallen! The ones who will remember them...are us, the living! We die trusting the living who follow to find meaning in our lives! That is the sole method which we can rebel against this cruel world!
My soldiers, rage! My soldiers, scream! My soldiers, fight!
""" #From an anime called "Attack on Titan" or "Shingeki no Kyojin" that I enjoy quite a bit. One of my favorite speeches from a man named Erwin Smith making a last stand against unbeatable and unthinkable circumstances that spell nothing but his and his soldiers' deaths.

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

def countE(es):
    words = 0
    for word in es:
        if "e" in word:
            words += 1
    
    return words


wds = remove_punctuation(erwinsSpeech).split(" ")
print("Your text contains ",len(wds)," words, of which ",countE(wds)," (",(countE(wds)/len(wds)) * 100,"%) contain an 'e'")