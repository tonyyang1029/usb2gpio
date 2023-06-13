# This is a sample Python script.
import decimal

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import blackscreenhunter_screenoff
import blackscreenhunter_reboot
import blackscreenhunter_poweroff

testmod = 0


def choose_test_mode():
    print('Please choose test mode:')
    print('1. Turn off/on screen repeatedly')
    print('2. Reboot device repeatedly')
    print('3. Power off/on device repeatedly')
    global testmod
    testmod = decimal.Decimal(input('Please input 1 ~ 3: '))
    if testmod > 3 or testmod < 1:
        print('The test mode [%d] is not correct!!' % testmod)
        exit(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    choose_test_mode()
    if testmod == 1:
        blackscreenhunter_screenoff.blackscreenhunter_screenoff()
    elif testmod == 2:
        blackscreenhunter_reboot.blackscreenhunter_reboot()
    elif testmod == 3:
        blackscreenhunter_poweroff.blackscreenhunter_poweroff()
    else:
        exit(1)
