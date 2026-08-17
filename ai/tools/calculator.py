from ai.tools.base import Tool


class CalculatorTool(Tool):
    
    @property
    def name(self) -> str:
        return "calculator"
        
    @property
    def description(self) -> str:
        return "Performs basic mathematical calculations."
        
    def execute(self, **kwargs) -> str:
        expression = kwargs["expression"]
        
        return str(eval(expression))
