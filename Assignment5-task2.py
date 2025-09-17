created_list = [i for i in range(1,11)]
print(f"Original list: {created_list}")
extracted_list = created_list[0:5]
print(f"Extracted first five elements: {extracted_list}")
extracted_list.reverse()
print(f"Reversed extracted elements: {extracted_list}")