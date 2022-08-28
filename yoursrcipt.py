import click
import dimod

@click.command()

def cli():
    ### Matrix
    #    0  1
    # 0 -1  2
    # 1  -  1
    bqm = dimod.BinaryQuadraticModel({0: -1, 1: 1}, {(0, 1): 2}, 0.0, dimod.BINARY)
    sampleset = dimod.ExactSolver().sample(bqm)
    print(sampleset)

if __name__ == '__main__':
    cli()
