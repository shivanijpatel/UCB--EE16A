import scipy.io

def loadWaveforms():
    MATLAB_FILE_NAME = 'waveforms.mat'
    mat_file = scipy.io.loadmat(MATLAB_FILE_NAME)
    time = mat_file['time'];
    s1_voltage = mat_file['s1_voltage'];
    s2_voltage = mat_file['s2_voltage'];
    s3_voltage = mat_file['s3_voltage'];
    return time,s1_voltage,s2_voltage,s3_voltage;
