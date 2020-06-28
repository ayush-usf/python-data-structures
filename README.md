<details>
    <summary>Virtual Environment (Conda) Setup</summary>
    
    # Creating the virtual environment with conda
    conda create --prefix=venv python

    # Activating environment
    conda activate ./venv 
    source activate /Users/..../venv

    # Deactivating environment
    conda deactivate
</details>

---
#### Ternary operator
```
val =  first_val if ternary_condition else second_val
```
#### Switch statement with lambdas
```
        {
            "case1": lambda x: operation1 (can be be independent of x),
            "case2": lambda x: operation2 ,
            "case3": lambda x: operation3 ,
            "case4": lambda x: operation4
        }[case_name](argument_x_for_lambda_func)
 ```
 ### If result required from switch statement
```
 result = {
            "case1": lambda x: op1 (can be be independent of x, but must return some value),
            "case2": lambda x: x * 2 ,
            "case3": lambda x: x + 2 ,
            "case4": lambda x: x - 1
        }[case_name](argument_x_for_lambda_func)
```