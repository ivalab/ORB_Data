clear all

addpath('/home/yipuzhao/Codes/VSLAM/TUM_VI_DatasetTools')

fps = 30.0

seq_list = {
  'living_room_traj0';
  'living_room_traj1';
  'living_room_traj2';
  'living_room_traj3';
  %
  'office_room_traj0';
  'office_room_traj1';
  'office_room_traj2';
  'office_room_traj3';
  };

for sn=1:length(seq_list)
  
  dat = textread([seq_list{sn} '.gt.freiburg']);
  
  dat(:, 1) = dat(:, 1) / fps;
  
  %% plot the x-y track
  figure(99);
  clf
  hold on
  for i=1:20:size(dat, 1)
    if i == 1
      plotPose(dat(i, 2:4), [dat(i, 8) dat(i, 5:7)], 'base', 0.5)
    else
      %   plot(pose_arr(:,2), pose_arr(:,3))
      plotPose(dat(i, 2:4), [dat(i, 8) dat(i, 5:7)], '', 0.15)
    end
  end
  axis equal
  
  %% save to text
  fileID = fopen([seq_list{sn} '_tum.txt'], 'w');
  
  fprintf(fileID, '#TimeStamp Tx Ty Tz Qx Qy Qz Qw\n');
  
  for i=1:size(dat, 1)
    %
    fprintf(fileID, '%.06f', dat(i, 1));
    for j=2:size(dat, 2)
      fprintf(fileID, ' %.07f', dat(i, j));
    end
    fprintf(fileID, '\n');
  end
  
  fclose(fileID);
  
end