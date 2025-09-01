import random
import string

POSSIBLE_CHARS = string.ascii_lowercase + string.digits + ' '

def validate_input(phrase):
    """Valida se a frase contém apenas os caracteres permitidos."""
    return all(char in POSSIBLE_CHARS for char in phrase)

def generate_random_phrase(length):
    """Gera uma frase aleatória com um determinado comprimento."""
    return ''.join(random.choice(POSSIBLE_CHARS) for _ in range(length))

def mutate_phrase(phrase, mutation_rate=0.05):
    """Muta aleatoriamente uma frase com base na taxa de mutação."""
    new_phrase = []
    for char in phrase:
        if random.random() < mutation_rate:
            new_phrase.append(random.choice(POSSIBLE_CHARS))
        else:
            new_phrase.append(char)
    return ''.join(new_phrase)

def reproduce(best_candidate, population_size=100, mutation_rate=0.05):
    """Cria uma população de frases mutadas a partir do melhor candidato."""
    return [mutate_phrase(best_candidate, mutation_rate) for _ in range(population_size)]

def select_best(population, target_phrase):
    """Seleciona o melhor candidato da população com base na semelhança com o alvo."""
    best_score = -1
    best_candidate = ''
    for phrase in population:
        score = sum(1 for a, b in zip(phrase, target_phrase) if a == b)
        if score > best_score:
            best_score = score
            best_candidate = phrase
    return best_candidate, best_score
