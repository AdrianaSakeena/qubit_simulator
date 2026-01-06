import src.state as state

def main():
    normalized, normalized_vector = state.normalized_complex_vector()
    if normalized == True:
        state.measurement_probability(normalized_vector)


if __name__ == "__main__":
    main()