shoot_range = []
shooter = [0, 0]
target_number = 0
hit_target_positions = []
targets = 0

for row in range(5):
    shoot_range.append(input().split())
    for col in range(5):
        if shoot_range[row][col] == 'A':
            shooter = [row, col]
        if shoot_range[row][col] == 'x':
            target_number += 1
            targets += 1

command_number = int(input())

while target_number > 0 and command_number > 0:
    command = input().split()
    shooter_r = shooter[0]
    shooter_c = shooter[1]
    command_number -= 1
    if len(command) > 2:
        steps = int(command[2])
    if command[1] == 'right':
        if len(command) > 2:
            if 0 <= shooter_c + steps < 5 and shoot_range[shooter_r][shooter_c + steps] == '.':
                shooter[1] = shooter_c + steps
            else:
                continue
        else:
            for shot in range(1, 5 - shooter_c):
                if shoot_range[shooter_r][shooter_c + shot] != '.':
                    shoot_range[shooter_r][shooter_c + shot] = '.'
                    hit_target_positions.append([shooter_r, shooter_c + shot])
                    target_number -= 1
                    break
    elif command[1] == 'left':
        if len(command) > 2:
            if 0 <= shooter_c - steps < 5 and shoot_range[shooter_r][shooter_c - steps] == '.':
                shooter[1] = shooter_c - steps
            else:
                continue
        else:
            for shot in range(1, shooter_c + 1):
                if shoot_range[shooter_r][shooter_c - shot] != '.':
                    shoot_range[shooter_r][shooter_c - shot] = '.'
                    hit_target_positions.append([shooter_r, shooter_c - shot])
                    target_number -= 1
                    break
    elif command[1] == 'up':
        if len(command) > 2:
            if 0 <= shooter_r - steps < 5 and shoot_range[shooter_r - steps][shooter_c] == '.':
                shooter[0] = shooter_r - steps
            else:
                continue
        else:
            for shot in range(1, shooter_r + 1):
                if shoot_range[shooter_r - shot][shooter_c] != '.':
                    shoot_range[shooter_r - shot][shooter_c] = '.'
                    hit_target_positions.append([shooter_r - shot, shooter_c])
                    target_number -= 1
                    break
    elif command[1] == 'down':
        if len(command) > 2:
            if 0 <= shooter_r + steps < 5 and shoot_range[shooter_r + steps][shooter_c] == '.':
                shooter[0] = shooter_r + steps
            else:
                continue
        else:
            for shot in range(1, 5 - shooter_r):
                if shoot_range[shooter_r + shot][shooter_c] != '.':
                    shoot_range[shooter_r + shot][shooter_c] = '.'
                    hit_target_positions.append([shooter_r + shot, shooter_c])
                    target_number -= 1
                    break
if target_number < 1:
    print(f'Training completed! All {targets} targets hit.')
else:
    print(f'Training not completed! {target_number} targets left.')
print(*hit_target_positions, sep='\n')