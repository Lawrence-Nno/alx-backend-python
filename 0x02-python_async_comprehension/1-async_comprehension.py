#!/usr/bin/env python3
""" Async comprehension """
from typing import List
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine will collect 10 random numbers using an
    async comprehensing over async_generator
    Returns:
        List[float]: return the 10 random numbers
    """
    result = [i async for i in async_generator()]
    return result
