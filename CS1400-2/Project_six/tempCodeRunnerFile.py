    walk_lyst = []
    for walk in argv[1]:
        try:
            walk_lyst.append(int(walk))
        except:
            pass
        
    trial_count = int(argv[2])
    walker = argv[3]
    print(argv[1])
    print(argv[2])
    print(argv[3])
    simulate(walk_lyst, trial_count, walker)