# python-data-structures

## Creating the virtual environment with conda
```
conda create --prefix=venv python
```

### Activating environment
```
conda activate ./venv 
source activate /Users/..../venv
```

### Deactivating environment
```
conda deactivate
```

### Ternary operator
```
val =  first_val if ternary_condition else second_val
```
### Switch statement with lambdas
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
            "case1": lambda x: operation1 (can be be independent of x),
            "case2": lambda x: operation2 ,
            "case3": lambda x: operation3 ,
            "case4": lambda x: operation4
        }[case_name](argument_x_for_lambda_func)
 ```
