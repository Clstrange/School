public class Reuse {
    Reuse Reuse(Reuse jim) {
        test:
            for (;;) {
                if (jim.Reuse(jim) == jim)
                    break test;
            }
            return jim;
    }
}
