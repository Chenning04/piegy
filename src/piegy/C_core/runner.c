#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>

#include "model.h"
#include "patch.h"
#include "sim_funcs.h"
//#include "random.h"



int main() {
    size_t N = 1;
    size_t M = 100;
    double maxtime = 100;
    double record_itv = 0.1;
    size_t sim_time = 5;
    bool boundary = true;
    uint32_t I_single[2] = {400, 200};
    double X_single[4] = {-1, 4, 0, 2};
    double P_single[6] = {0.5, 0.5, 10, 10, 0.001, 0.001};
    int32_t print_pct = 25;
    int32_t seed = 36;  // -1 for None

    uint32_t I[N * M * 2];
    double X[N * M * 4];
    double P[N * M * 6];

    //printf("sizeof(patch_t) = %zu bytes\n", sizeof(patch_t));
    size_t ij = 0;
    for (size_t i = 0; i < N; i++) {
        for (size_t j = 0; j < M; j++) {
            I[ij * 2] = I_single[0];
            I[ij * 2 + 1] = I_single[1];

            for (size_t k = 0; k < 4; k++) {
                X[ij * 4 + k] = X_single[k];
            }
            for (size_t k = 0; k < 6; k++) {
                P[ij * 6 + k] = P_single[k];
            }
            ++ij;
        }
    }

    model_t* mod = malloc(sizeof(model_t));
    mod_init(mod, N, M, maxtime, record_itv, sim_time, boundary, I, X, P, print_pct, seed);

    char message[20] = "";  // writable buffer with enough space
    //uint8_t result = run(mod, message, 20);

    /*rand_init((uint64_t) 123456789);
    size_t how_many = 100000000000;
    double max = 0;
    double min = 1;

    size_t groups[10] = {0};

    for (size_t i = 0; i < how_many; i++) {
        double r = random01();
        if (r > max) {
            max = r;
        } else if (r < min) {
            min = r;
        }

        uint8_t r_int = r * 10;
        if (r_int > 9) r_int = 9;
        switch (r_int) {
            case 9:
                groups[9] += 1;
                break;
            case 8:
                groups[8] += 1;
                break;
            case 7:
                groups[7] += 1;
                break;
            case 6:
                groups[6] += 1;
                break;
            case 5:
                groups[5] += 1;
                break;
            case 4:
                groups[4] += 1;
                break;
            case 3:
                groups[3] += 1;
                break;
            case 2:
                groups[2] += 1;
                break;
            case 1:
                groups[1] += 1;
                break;
            default:
                groups[0] += 1;
                break;
        }
    }
    fprintf(stdout, "max is %.17f\n", max);
    fprintf(stdout, "min is %.17f\n", min);

    for (size_t i = 0; i < 10; i++) {
        fprintf(stdout, "%.10f\n", ((double) groups[i]) / (double) how_many);
    }*/

    /*for (size_t i = 0; i < mod->max_record; i++) {
        fprintf(stdout, "%f ", mod->U1d[i]);
    }
    fprintf(stdout, "\n");
    for (size_t i = 0; i < mod->max_record; i++) {
        fprintf(stdout, "%f ", mod->Upi_1d[i]);
    }*/
    mod_free(mod);
    mod = NULL;
}

